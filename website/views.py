from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):

	title = "<h1>Página en construcción</h1>"
	body = "<h3>Muy pronto estaremos en línea...</h3>"
	footer = "<h6>[+] Powered by M3t4l3rk L4bs.</h6>"

	return HttpResponse(title + body + footer)