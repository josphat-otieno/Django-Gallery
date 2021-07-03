from django.contrib import admin
from .models import Photographer, Category,Location,Images

# Register your models here.
admin.site.register(Photographer)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Images)

