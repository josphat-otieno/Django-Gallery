from django.test import TestCase
from .models import Photographer, Category, Location,Images
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

class ImageTestCase(TestCase):
    def setUp(self):
        self.nairobi =Location(location_name='nairobi')
        self.nairobi.save_location()
        self.travel =Category(category_name='travel')
        self.travel.save_category()

        self.new_image = Images(image_name='lion',image_description='lives in forest', location=self.nairobi, category=self.travel)
        self.new_image.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Images))

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Images.objects.all().delete()

    def test_save_images(self):
        self.new_image.save_image()
        images = Images.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_images(self):
        self.new_image.save_image()
        images = Images.objects.all()
        self.new_image.delete_image()
        self.assertTrue(len(images)==0)

    def test_update_image(self):
        self.new_image.save_image()
        self.new_image.update_image(self.new_image.id, 'photos/test.jpg')
        image_changed = Images.objects.filter(image_name='photo/test.jpg')
        self.new_image.save_image()
        self.assertTrue(image_changed,Images)

    def test_get_image_by_id(self):
        image= self.new_image.get_image_by_id(self.new_image.id)
        images = Images.objects.filter(id=self.new_image.id)
        self.assertTrue(image, images)

    def test_search_image_by_location(self):
        self.new_image.save_image()
        found_images = self.new_image.get_images_by_location(location='nairobi')
        self.assertTrue(len(found_images) == 1)

    def test_get_image_by_category(self):
        category = 'food'
        images= self.new_image.search_image_by_category(category)
        self.assertTrue(len(images)==1)

   







       

