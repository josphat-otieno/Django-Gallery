from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Category, Location, Images

# Create your views here.
def index(request):

    images = Images.objects.all()
    categories = Category.objects.all()
    locations = Location.objects.all()
    context= {"images": images, "categories":categories, "locations":locations}
    return render(request, 'all-gallery/index.html', context)