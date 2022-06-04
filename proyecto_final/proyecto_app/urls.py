from django.urls import path, include

from proyecto_app.views import productos, usuarios, descripcion

urlpatterns = [
    path("productos/", productos, name="productos"),
    path("usuarios/", usuarios, name="usuarios"),
    path("descripcion/", descripcion, name="descripcion")
]