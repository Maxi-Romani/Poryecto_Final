from django.shortcuts import render
from proyecto_app.models import Productos

# Create your views here.

def proyecto_app(request):
    print(request.method)
    productos = Productos.objects.all()
    context = {'productos':productos}
    return render(request, 'products.html', context=context)
    