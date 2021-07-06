from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^image/(\d+)/$',views.image,name ='image'),
    url(r'^search/', views.search_results, name='search_results'),
     url(r'^category/(\w+)', views.get_category,name='get_category'),
    url(r'^location/(?P<location>\w+)', views.get_images_by_location, name='get_images_by_location'),
   
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)