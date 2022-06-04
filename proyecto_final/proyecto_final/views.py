from django.http import HttpResponse
from django.shortcuts import render

def productos(request):
	return HttpResponse ("productos")

def usuarios(request):
	return HttpResponse ("usuarios")

def descripcion(request):
	return HttpResponse ("descripcion")
   
