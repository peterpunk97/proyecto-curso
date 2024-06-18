from django.contrib import admin
from django.urls import path
from inicio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name="Principal"),
    path('contacto/', views.contacto, name="Contacto"),
    path('cursos/', views.cursos, name="Cursos"), 
]
