from django.urls import path

from orders.views import (CancelTemplateView, CreateOrderView, OrderDetailView,
                          OrderListView, SuccessTemplateView)

app_name = 'orders'

urlpatterns = [
    path('', OrderListView.as_view(), name='orders'),
    path('detail/<int:pk>/', OrderDetailView.as_view(), name='orders_details'),
    path('create_order/', CreateOrderView.as_view(), name='create_order'),
    path('order-success/', SuccessTemplateView.as_view(), name='order_success'),
    path('order-cancel/', CancelTemplateView.as_view(), name='order_canceling'),
]
