from django.db import models

# Create your models here.
class Photographer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name

    def save_photographer(self):
        self.save()

    def delete_photographer(self):
        self.delete()

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Images(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image = models.ImageField(upload_to='galleries/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls):
        image = cls.objects.filter(id).update()
        return image
        # Editor.objects.filter(id = 2).update(first_name ='Kim')

    @classmethod
    def get_image_by_id(cls, image_id):
        image= cls.objects.filter(id = image_id)
        return image


    @classmethod
    def search_image_by_category(cls, category):
        pass

    @classmethod
    def filter_image_by_location(cls):
        pass
    # def days_news(cls,date):
    #     news = cls.objects.filter(pub_date__date = date)
    #     return news

        

        
