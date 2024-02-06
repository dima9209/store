import stripe
from http import HTTPStatus

from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from common.view import TitleMixin
from orders.forms import CreateOrderForm
from products.models import Basket
from orders.models import Order


stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/success.html'
    title = 'Store - Спасибо за заказ'


class CancelTemplateView(TemplateView):
    template_name = 'orders/canceled.html'


class OrderListView(TitleMixin, ListView):
    title = 'Store-Заказы'
    template_name = 'orders/orders.html'
    queryset = Order.objects.all()
    ordering = ('-id')

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        return queryset.filter(initiator=self.request.user)


class CreateOrderView(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    form_class = CreateOrderForm
    title = 'Store - Оформление заказа'
    success_url = reverse_lazy('orders:create_order')
    
    def post(self, request, *args, **kwargs):
        super(CreateOrderView, self).post(request, *args, **kwargs)
        baskets = Basket.objects.filter(user=self.request.user)
        checkout_session = stripe.checkout.Session.create(
            line_items=baskets.stripe_products(),
            metadata={'order_id': self.object.id},
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_success')),
            cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_canceling'))
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(CreateOrderView, self).form_valid(form)


@csrf_exempt
def stripe_webhook_view(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fulfill the purchase...
        fulfill_order(session)

    # Passed signature verification
    return HttpResponse(status=200)


def fulfill_order(session):
    order_id = int(session.metadata.order_id)
    order = Order.objects.get(id=order_id)
    order.update_after_payment()
