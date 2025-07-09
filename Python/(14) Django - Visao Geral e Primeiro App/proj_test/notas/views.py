'''from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
   template = loader.get_template('notas/index.html')
   context = {'texto': 'Hello, world! Este é o meu primeiro app DJANGO',}

   return HttpResponse(template.render(context, request))'''

from django.shortcuts import render
from .models import Nota

def index(request):
   titulo = 'Hello, world! Este é o meu primeiro app DJANGO'
   notas = Nota.objects.all()

   context = {
      'titulo': titulo,
      'notas': notas
   }

   return render(request, 'notas/index.html', context)