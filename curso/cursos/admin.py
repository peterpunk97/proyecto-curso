from django.contrib import admin
from.models import Curso


class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('idCurso', 'nombreCurso', 'fechaInicio')
    search_fields = ('idCurso', 'nombreCurso','fechaInicio')
    date_hierarchy = 'created'
    list_filter = ('idCurso', 'nombreCurso', 'fechaInicio')
admin.site.register(Curso, AdministrarModelo)

