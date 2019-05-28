from rest_framework import serializers

from .models import City


class CitySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    description = serializers.CharField()
    country_id = serializers.IntegerField()
    
    def create(self, validated_data):
        return City.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.country_id = validated_data.get('country_id', instance.country_id)
        instance.save()
        return instance

    