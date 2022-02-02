from django.test import TestCase

from .models import Ingredients
# Create your tests here.


class IngredientsModelTest(TestCase):
    """
    Tests for the Ingredients model
    """

    def setUpTestData():
        Ingredients.objects.create(name='Ingredient',)

    def test_ingredient_name_label(self):
        ingredient = Ingredients.objects.get(id=1)
        field_label = ingredient._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')
        return

    def test_ingredient_name_max_length(self):
        ingredient = Ingredients.objects.get(id=1)
        max_length = ingredient._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)
        return
