from django.urls import path

from orders.views import CreateOrderView, SuccessTemplateView, CancelTemplateView


app_name = 'orders'

urlpatterns = [
    path('create_order/', CreateOrderView.as_view(), name='create_order'),
    path('order-success/', SuccessTemplateView.as_view(), name='order_success'),
    path('order-cancel/', CancelTemplateView.as_view(), name='order_canceling'),
]
