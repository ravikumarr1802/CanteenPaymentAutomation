import json
from django.shortcuts import render,redirect
from django.views import View
from .models import MenuItem,Orderr

class Index(View):
    def get(self,request,*args,**kwargs):
        return render(request,'customer/index.html')
    
class Order(View):
    
    def get(self,request,*args,**kwargs):
        Tiffins = MenuItem.objects.filter(category__name__icontains = 'Tiffin')
        Lunch = MenuItem.objects.filter(category__name__icontains = 'Lunch')
        Fast_Food = MenuItem.objects.filter(category__name__icontains = 'Fast Food')

        context = {
            'tiffins' : Tiffins,
            'lunch' : Lunch,
            'Fast_Food': Fast_Food
        }
        return render(request,'customer/order.html',context=context)
    
    def post(self, request, *args, **kwargs):
        order_items = {'items': []}
        name = request.POST.get('name')
        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk = int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }
            order_items['items'].append(item_data)

        price = 0
        item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = Orderr.objects.create(price=price,name = name)
        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price
        }

        return redirect('order-confirmation', pk=order.pk)


class OrderConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = Orderr.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
        }

        return render(request, 'customer/order_confirmation.html', context)

    def post(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)

        if data['isPaid']:
            order = Orderr.objects.get(pk=pk)
            order.is_paid = True
            order.save()

        return redirect('payment-confirmation')

class OrderPayConfirmation(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/order_pay_confirmation.html')