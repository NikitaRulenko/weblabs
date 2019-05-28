from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import City
from .serializers import CitySerializer

class CityView(APIView):

    def get_queryset(self, pk):
        try:
            city = City.objects.get(pk=pk)
        except City.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return city
    
    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response({"cities": serializer.data})  

    def post(self, request):
        city = request.data.get('city')
        # Create an article from the above data
        serializer = CitySerializer(data=city)
        
        if serializer.is_valid(raise_exception=True):
            city_saved = serializer.save()
        return Response({"success": "City '{}' created successfully".format(city_saved.name)})    

    def put(self, request, pk):
        saved_city = get_object_or_404(City.objects.all(), pk=pk)
        data = request.data.get('city')
        serializer = CitySerializer(instance=saved_city, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            city_saved = serializer.save()
        return Response({
            "success": "City '{}' updated successfully".format(city_saved.name)
        }) 

    def delete(self, request, pk):
    # Get object with this pk
        city = get_object_or_404(City.objects.all(), pk=pk)
        city.delete()
        return Response({
            "message": "City with id `{}` has been deleted.".format(pk)
        }, status=204)    