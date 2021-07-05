from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Category, Location, Images
import pyperclip

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


def get_image_by_location(request,loc):
    my_images = Images.get_image_by_location(loc)
    print(my_images)
    return render(request, 'location.html', {"my_images": my_images})

def copy_to_clipboard(request):
    pyperclip.copy(image)

def search_results(request):
    pass

def search_results(request):
    
    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Images.search_image_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"all_images": searched_images})

    else:
        message = "You haven't searched for any category"
        return render(request, 'all-gallery/search.html',{"message":message})


    