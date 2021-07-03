from django.test import TestCase
from .models import Photographer, Category, Location
# Create your tests here.


class PhotographerTestClass(TestCase):
    def setUp(self):
        self.josephat = Photographer(first_name = 'Josephat', last_name='Otieno', email='josephatotieno92@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.josephat, Photographer))

    def test_save_method(self):
        self.josephat.save_photographer()
        photogarphers = Photographer.objects.all()
        self.assertTrue(len(photogarphers)>0)

    def test_delete_method(self):
        self.josephat.save_photographer()
        photographers = Photographer.objects.all()
        self.josephat.delete_photographer()
        self.assertTrue(len(photographers)==0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.new_category = Category(category_name="Vacation")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_category, Category))

    def test_save_category(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    def test_delete_category(self):
        self.new_category.save_category()
        categories = Category.objects.all()
        self.new_category.delete_category()
        self.assertTrue(len(categories)==0)

class LocationTestClass(TestCase):
    def setUp(self):
        self.new_location = Location(location_name="Nairobi")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location, Location))

    def test_save_location(self):
        self.new_location.save_location()
        locations= Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_category(self):
        self.new_location.save_location()
        locations= Location.objects.all()
        self.new_location.delete_location()
        self.assertTrue(len(locations)==0)


       

