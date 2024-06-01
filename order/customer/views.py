from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self,request,*args,**kwargs):
        return render(request,'customer/index.html')

class About(View):
    def get(self,request,*args,**kwargs):
        return render(request,'customer/base.html')
    
class Order(View):
    def get(self,request,*args,**kwargs):
        Tiffins = MenuItem.objects.filter(category_name_contains = 'Tiffin')
        # Lunch = MenuItem.objects.filter(category_name_contains = 'Lunch')
        # Fast Food = MenuItem.objects.filter(category_name_contains = 'Fast Food')

        context = {
            
        }


