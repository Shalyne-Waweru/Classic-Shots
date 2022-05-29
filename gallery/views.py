from django.shortcuts import render
from django.http  import HttpResponse,Http404
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
  locations = Location.all_locations()

  if 'locations' in request.GET and request.GET['locations']:
        locationName = request.GET.get('locations')
        images = Image.filter_images_by_location(locationName)

  return render(request, 'gallery.html', {'images' : images, 'locations' : locations})