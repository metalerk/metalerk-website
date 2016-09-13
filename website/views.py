from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):

	title = "<h1>Página en construcción</h1>"
	body = "<h3>Muy pronto estaremos en línea...</h3>"

	return HttpResponse(title + body)