from django.db import models

class Post(models.Model):

	titulo = models.CharField(max_length=120)
	contenido = models.TextField(max_length=500)
	actualizado = models.DateTimeField(auto_now=True, auto_now_add=False)
	registro = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.titulo