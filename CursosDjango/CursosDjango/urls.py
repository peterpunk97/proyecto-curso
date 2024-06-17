from django.conf import settings
from django.contrib import admin
from django.urls import path
from contenido import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.principal, name="principal"),
    path('cursos/',views.cursos, name="cursos"),
    path('contacto/',views.contacto, name="contacto"),
]

if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)