from django.contrib import admin
from django.urls import path
from django.conf import settings
from inicio import views
from cursos import views as views_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cursos/', views_cursos.registroCursos, name="Cursos" ),
    path('', views.principal, name="Principal"),
    path('contacto/', views.contacto, name="Contacto"),
    path('cursos/', views.cursos, name="Cursos"), 
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)