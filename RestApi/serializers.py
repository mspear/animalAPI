from RestApi.models import Animal
from rest_framework import serializers


class PartialAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('imageURL', 'id', 'commonName')


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('id', 'imageURL', 'commonName', 'scientificName', 'family')

    def create(self, validated_data):
        return Animal.objects.create(**validated_data)
