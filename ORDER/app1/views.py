from django.shortcuts import render


def index(request):
    return render(request, 'temp/index.html')

def contact(request):
    method = request.method
    return render(request,'temp/contact.html',{"method": method})