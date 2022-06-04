from django.shortcuts import render
from proyecto_app.models import Productos, Usuarios, Descripcion

# Create your views here.

def productos(request):
    print(request.method)
    productos = Productos.objects.all()
    context = {'productos':productos}
    return render(request, 'productos.html', context=context)

def usuarios(request):
    print(request.method)
    usuarios = Usuarios.objects.all()
    context = {'usuarios':usuarios}
    return render(request, 'usuarios.html', context=context)

def descripcion(request):
    print(request.method)
    descripcion = Descripcion.objects.all()
    context = {'descripcion':descripcion}
    return render(request, 'descripcion.html', context=context)

