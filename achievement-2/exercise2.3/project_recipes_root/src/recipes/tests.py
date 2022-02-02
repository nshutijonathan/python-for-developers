from django.test import TestCase
from .models import Recipes
# Create your tests here.


class RecipesModelTest(TestCase):
    """
    Tests for the Recipes model
    """

    def setUpTestData():
        Recipes.objects.create(name='Recipe',)

    def test_recipe_name_label(self):
        recipe = Recipes.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
        return

    def test_recipe_name_max_length(self):
        recipe = Recipes.objects.get(id=1)
        max_length = recipe._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)
        return
