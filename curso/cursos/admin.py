from django.contrib import admin
from.models import Curso
from.models import Actividad


class AdministrarCurso(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('idCurso', 'nombreCurso', 'fechaInicio')
    search_fields = ('idCurso', 'nombreCurso', 'fechaInicio')
    date_hierarchy = 'created'
    list_filter = ('idCurso', 'nombreCurso', 'fechaInicio')
    list_per_page=2
    list_editable=('nombreCurso',)

admin.site.register(Curso, AdministrarCurso)


class AdministrarActividad(admin.ModelAdmin):
    readonly_fields = ('fechaCreacion',)
    list_display = ('claveActividad',  'descripcion', 'fechaCreacion')
    search_fields = ('claveActividad', 'fechaCreacion')
    date_hierarchy = 'fechaCreacion'
    list_filter = ('claveActividad', 'nombreCurso', 'fechaCreacion')
    list_per_page=2
    list_editable=('descripcion',)

admin.site.register(Actividad, AdministrarActividad)



