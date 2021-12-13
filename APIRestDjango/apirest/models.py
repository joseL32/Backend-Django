from django.db import models

class Cuestionario(models.Model):

    preguntas=models.CharField(max_length=200)
    respuestas=models.CharField(max_length=100)

    class Meta:
        verbose_name =("Cuestionario")
        verbose_name_plural =("Cuestionarios")

    def __str__(self):
        return self.preguntas

    