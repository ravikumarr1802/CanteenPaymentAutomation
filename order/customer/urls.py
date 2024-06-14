from django.urls import path
from .views import * 

urlpatterns = [
   path('',Index.as_view(),name= 'index'),
   path('Order/',Order.as_view(),name= 'order'),
   path('order-confirmation/<int:pk>', OrderConfirmation.as_view(),
         name='order-confirmation'),
    path('payment-confirmation/', OrderPayConfirmation.as_view(),
         name='payment-confirmation'),
]
