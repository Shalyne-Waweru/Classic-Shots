from django.shortcuts import render
from django.http  import HttpResponse
from .models import *

def home(request):
  '''
  View function that returns the home page and its data
  '''
  return render(request, 'index.html', {})

def gallery(request):
  '''
  View function that returns the gallery page and its data
  '''
  images = Image.all_images()
  return render(request, 'gallery.html', {'images' : images} )
