from django.db import models

class Post:

	titulo = models.CharField(max_length=120)
	contenido = models.TextField(max_length=1000)
	actualizado = models.DateField(auto_now=True, auto_now_add=False)
	registro = models.DateField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title