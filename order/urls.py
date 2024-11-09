from django.urls import path
from .views import CreateOrderView, ConfirmPaymentView

urlpatterns = [
    path('orders/create/', CreateOrderView.as_view(), name='order-create'),
    path('orders/confirm-payment/', ConfirmPaymentView.as_view(), name='confirm-payment'),
]
