from django.db import models


class Country(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()

  def __str__(self):
        return self.name

  def get_name(self):
        return self.name    

  def get_description(self):
        return self.description         

class City(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    country = models.ForeignKey('Country', related_name='cities', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_description(self):
        return self.name + ' description: ' + self.description 

    def get_name(self):
        return self.name       

    def get_country(self):
        return self.country_id     

        