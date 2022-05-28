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