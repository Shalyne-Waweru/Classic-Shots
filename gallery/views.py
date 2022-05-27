from django.shortcuts import render
from django.http  import HttpResponse

def home(request):
  '''
  View function that returns the home page and its data
  '''
  return render(request, 'index.html', {})

def gallery(request):
  '''
  View function that returns the gallery page and its data
  '''
  return render(request, 'gallery.html', {})
