from django.shortcuts import render
from django.views import View
from django.utils.timezone import datetime
from customer.models import Orderr

class Dashboard(View):
    def get(self, request, *args, **kwargs):
        today = datetime.today()
        orders = Orderr.objects.filter(
            created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)
        orderstobegiven = []
        for order in orders:

            if not order.ordergiven:
                orderstobegiven.append(order)

        context = {
            'orders': orderstobegiven,
        }
        return render(request, 'restaurant/dashboard.html', context)

    def test_func(self):
        return True

class OrderDetails(View):
    def get(self, request, pk, *args, **kwargs):
        order = Orderr.objects.get(pk=pk)
        context = {
            'order': order
        }
        return render(request, 'restaurant/order-details.html', context)

    def post(self, request, pk, *args, **kwargs):
        order = Orderr.objects.get(pk=pk)
        order.ordergiven = True
        order.save()

        context = {
            'order': order
        }

        return render(request, 'restaurant/order-details.html', context)

    def test_func(self):
        return True