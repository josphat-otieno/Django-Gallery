from django.db import models
from django.db.models.fields import CharField, EmailField

# Create your models here.
class Photographer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = EmailField()
    
    def __str__(self):
        return self.first_name

