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
    path('consulta1/', views_cursos.consultar1, name="Consulta1"),
    path('consulta2/', views_cursos.consultar2, name="Consulta2"),
    path('consulta3/', views_cursos.consultar3, name="Consulta3"),
    path('consulta4/', views_cursos.consultar4, name="Consulta4"),
    path('consulta5/', views_cursos.consultar5, name="Consulta5"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)