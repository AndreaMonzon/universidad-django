from django import views
from django.urls import URLPattern, path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('registrarCurso/',views.registrarCurso),
    path('eliminarCurso/<codigo>',views.eliminarCurso,name='eliminar'),
    path('edicionCurso/',views.edicionCurso),
    path('editarCurso/<codigo>',views.editarCurso,name='editar'),
]