from unicodedata import category
from django.test import TestCase
from .models import Category,Location,Image

class CategoryTestClass(TestCase):
    '''
    Test class that defines test cases for the model behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        It defines instructions that will be executed before each test method.
        '''
        self.new_category = Category(categoryName = 'food')

    # FIRST TEST
    def test_instance(self):
        '''
        test_instance test case to test if the object is initialized properly
        '''
        self.assertTrue(isinstance(self.new_category,Category))

    # SECOND TEST
    def test_save_category(self):
        '''
        test_save_category test case to test if the object is being saved correctly
        '''
        self.new_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    # THIRD TEST
    def test_update_category(self):
        '''
        test_update_category test case to test if the object is being updated correctly
        '''
        self.new_category.save_category()
        self.new_category.categoryName = 'Meals'
        self.assertTrue(self.new_category.categoryName == 'Meals')

    # FOURTH TEST
    def test_delete_category(self):
        '''
        test_delete_category test case to test if the object is being deleted correctly
        '''
        self.new_category.save_category()
        self.new_category.delete_category()
        self.assertTrue(len(Category.objects.all()) == 0)

class LocationTestClass(TestCase):
    '''
    Test class that defines test cases for the model behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        It defines instructions that will be executed before each test method.
        '''
        self.new_location = Location(locationName = 'Nairobi')

    # FIRST TEST
    def test_instance(self):
        '''
        test_instance test case to test if the object is initialized properly
        '''
        self.assertTrue(isinstance(self.new_location,Location))

    # SECOND TEST
    def test_save_location(self):
        '''
        test_save_location test case to test if the object is being saved correctly
        '''
        self.new_location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    # THIRD TEST
    def test_update_location(self):
        '''
        test_update_location test case to test if the object is being updated correctly
        '''
        self.new_location.save_location()
        self.new_location.locationName = 'Nrb'
        self.assertTrue(self.new_location.locationName == 'Nrb')

    # FOURTH TEST
    def test_delete_location(self):
        '''
        test_delete_location test case to test if the object is being deleted correctly
        '''
        self.new_location.save_location()
        self.new_location.delete_location()
        self.assertTrue(len(Location.objects.all()) == 0)

class ImageTestClass(TestCase):
    '''
    Test class that defines test cases for the model behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
      '''
      Set up method to run before each test cases.
      It defines instructions that will be executed before each test method.
      '''

      # Creating and save a new category and location
      self.new_category = Category.objects.create(categoryName = 'food')
      self.new_location = Location.objects.create(locationName = 'Nairobi')

      self.new_image= Image(image = 'media/gallery-images/img1.jpg', title = "Image Title", description = "Image description", category = self.new_category, location = self.new_location)

    # FIRST TEST
    def test_instance(self):
        '''
        test_instance test case to test if the object is initialized properly
        '''
        self.assertTrue(isinstance(self.new_image,Image))

    # SECOND TEST
    def test_save_image(self):
        '''
        test_save_image test case to test if the object is being saved correctly
        '''
        self.new_image.save_image()
        gallery_images = Image.objects.all()
        self.assertTrue(len(gallery_images) > 0)

    # THIRD TEST
    def test_update_image(self):
        '''
        test_update_image test case to test if the object is being updated correctly
        '''
        self.new_image.save_image()
        self.new_image.title = 'New Image Title'
        self.assertTrue(self.new_image.title == 'New Image Title')

    # FOURTH TEST
    def test_delete_image(self):
        '''
        test_delete_image test case to test if the object is being deleted correctly
        '''
        self.new_image.save_image()
        self.new_image.delete_image()
        self.assertTrue(len(Image.objects.all()) == 0)

    # FIFTH TEST
    def test_get_image_by_id(self):
        '''
        test_get_image_by_id test case to test if the object is being retrieved correctly
        '''
        self.new_image.save_image()
        saved_image = Image.objects.filter(id=self.new_image.id)
        found_image = self.new_image.get_image_by_id(self.new_image.id)
        self.assertTrue(found_image, saved_image)

    # SIXTH TEST
    def test_search_image_by_category(self):
        '''
        test_search_image_by_category test case to test if the objects are being retrieved correctly
        '''
        self.new_image.save_image()
        searched_images = Image.search_images_by_category('food')
        self.assertTrue(len(searched_images) > 0)

    # SEVENTH TEST
    def test_filter_images_by_location(self):
      '''
      test_filter_images_by_location test case to test if the objects are being retrieved correctly
      '''
      self.new_image.save_image()
      found_images = Image.filter_images_by_location(self.new_location)
      self.assertTrue(len(found_images) > 0)