
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
    def update_image(cls, id,value):
        image = cls.objects.filter(id=id).update(image_name=value)
        return image
        # Editor.objects.filter(id = 2).update(first_name ='Kim')

    @classmethod
    def get_image_by_id(cls, image_id):
        image= cls.objects.filter(id = image_id)
        return image


    @classmethod
    def search_image_by_category(cls,search_term):
        search_result = cls.objects.filter(category__category_name__contains=search_term)
        return search_result

    

    @classmethod
    def get_images_by_location(cls,location):
        location_images = cls.objects.filter(location__location_name=location).all()
        return location_images

    

  
    # def days_news(cls,date):
    #     news = cls.objects.filter(pub_date__date = date)
    #     return news

    # Spanning multi-valued relationships¶
    # Blog.objects.filter(entry__headline__contains='Lennon')
    # Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)
    # Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)
    # Blog.objects.filter(entry__authors__name='Lennon')
    # # Blog.objects.filter(entry__headline__contains='Lennon')

    #lookups spanning relationship
    #  Entry.objects.filter(blog__name='Beatles Blog')


# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()

#     def __str__(self):
#         return self.name

# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name

# class Entry(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#     authors = models.ManyToManyField(Author)
#     number_of_comments = models.IntegerField()
#     number_of_pingbacks = models.IntegerField()
#     rating = models.IntegerField()

#     def __str__(self):
#         return self.headline

        

        
