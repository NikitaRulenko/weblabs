from django.test import TestCase, Client
from django.urls import reverse

from .views import CityView
from .models import City, Country
from .serializers import CitySerializer


# initialize the APIClient app
client = Client()

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

class GetAllCitiesTest(TestCase):
    
    def setUp(self):
        Country.objects.create(name = 'Dreamland', description = 'Somwhere_in_forest')
        Country.objects.create(name = 'Lapland', description = 'Somwhere_in_snow')
        Country.objects.create(name = 'Dankmir', description = 'Somwhere_in_swamp')

        City.objects.create(name = 'Pivo', description = 'temnoe', country_id = 1)

    def test_get_cities_url(self):    
        response = client.get('/api/cities/')
        self.assertEqual(response.status_code, 200)

    def test_post_wrong_city_data(self):
        response = client.post('/api/cities/', {'name': 'yoba', 'description': 'qwerty', 'country_id': 1})
        self.assertEqual(response.status_code, 400)

    def test_post_wrong_adress(self):
        response = client.post('cities/', {'name': 'yoba', 'description': 'qwerty', 'country_id': 1})
        self.assertEqual(response.status_code, 404)  

    def test_get_all_cities(self):
        response = client.get('/api/cities/')
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        self.assertEqual(response.data, {"cities": serializer.data})   

