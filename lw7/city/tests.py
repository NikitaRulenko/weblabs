import json
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

class APICitiesTest(TestCase):
    
    def setUp(self):
        Country.objects.create(name = 'Dreamland', description = 'Somwhere_in_forest')
        Country.objects.create(name = 'Lapland', description = 'Somwhere_in_snow')
        Country.objects.create(name = 'Dankmir', description = 'Somwhere_in_swamp')

        City.objects.create(name = 'Pivo', description = 'temnoe', country_id = 1)
        self.city = City.objects.create(name = 'Vodka', description = 'prozrachnaya', country_id = 1)

        self.valid_post_city = {"city":{"name":"poponya","description":"popopopo","country_id":1}}
        self.valid_put_city = {"city":{"name":"Vodka","description":"bubuka","country_id":1}}
        self.valid_delete_city = {"city":{"name":"Vodka","description":"bubuka","country_id":1}}

        self.put_city_check = {"city":{"name":"Vodka","description":"bubuka","country_id":1}}

    def test_get_cities_url(self):    
        response = client.get('/api/cities/')
        self.assertEqual(response.status_code, 200)

    def test_get_single_city_wrong_id(self):
        response = client.get('/api/cities/100500')
        self.assertEqual(response.status_code, 404)    

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

    def test_post_city(self):
        response = client.post('/api/cities/', data=json.dumps(self.valid_post_city), content_type='application/json')
        self.assertEqual(response.status_code, 200)
       
    def test_valid_put_city(self):
        response = client.put('/api/cities/'+str(self.city.pk), 
                   data=json.dumps(self.valid_put_city),
                   content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.valid_put_city, self.put_city_check)   

    def test_valid_delete_city(self):
        response = client.delete('/api/cities/'+str(self.city.pk), 
                   data=json.dumps(self.valid_delete_city),
                   content_type='application/json')
        self.assertEqual(response.status_code, 204) 

        response = client.delete('/api/cities/'+str(self.city.pk), 
                   data=json.dumps(self.valid_delete_city),
                   content_type='application/json')
        self.assertEqual(response.status_code, 404) 

        