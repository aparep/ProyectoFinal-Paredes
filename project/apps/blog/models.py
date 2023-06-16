from django.db import models

class Post(models.Model):
    Titulo = models.CharField(max_length=250)
    Contenido = models.CharField(max_length=400)
    Fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.Titulo

class Autor(models.Model):
    Autor = models.CharField(max_length=150)
    DNI = models.IntegerField()

    def __str__(self) -> str:
        return self.Autor
    

