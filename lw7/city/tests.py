from django.test import TestCase
from .models import City, Country


class CountryTest(TestCase):
    
    def setUp(self):
        Country.objects.create(name = 'Dreamland', description = 'Somwhere_in_forest')

    def test_country_name(self):
        country_yo = Country.objects.get(name = 'Dreamland')    
        self.assertEqual(country_yo.get_name(), 'Dreamland')

    def test_country_description(self):
        country_yo = Country.objects.get(name = 'Dreamland')
        self.assertEqual(country_yo.get_description(), 'Somwhere_in_forest')   

class CityTest(TestCase):

    def setUp(self):
        City.objects.create(name = 'Azgard', description = 'Vikings_Heaven', country_id = 1)

    def test_city_description(self):
        city_azgard = City.objects.get(name = 'Azgard')
        self.assertEqual(city_azgard.get_description(), 'Azgard description: Vikings_Heaven')

    def test_city_name(self):
        city_azgard = City.objects.get(name = 'Azgard')
        self.assertEqual(city_azgard.get_name(), 'Azgard')   

    def test_city_country(self):
        city_azgard = City.objects.get(name = 'Azgard')   
        self.assertEqual(city_azgard.get_country(), 1)            

