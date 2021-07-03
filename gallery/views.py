from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Category, Location, Images

# Create your views here.
def index(request):

    images = Images.objects.all()
    categories = Category.objects.all()
    locations = Location.objects.all()
    return render(request, 'all-gallery/index.html',  {"images": images, "categories":categories, "locations":locations})

def image(request,image_id):
    try:
        image = Images.objects.get(id = image_id)
    except Images.DoesNotExist:
        raise Http404()
    return render(request,"all-gallery/image.html", {"image":image})