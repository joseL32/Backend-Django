from django.contrib import admin
from .models import Cuestionario

class CuestionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'preguntas', 'respuestas')

admin.site.register(Cuestionario,CuestionarioAdmin)
