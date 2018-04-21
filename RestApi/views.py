from RestApi.models import Animal
from RestApi.serializers import AnimalSerializer, PartialAnimalSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

class AnimalListView(APIView):
    """
    Retrieve limited list data about the Animal List
    """

    def get_object(self, pk):
        return Animal.objects.get(pk)

    def get(self, request, format=None):
        animals = Animal.objects.all()
        serializer = PartialAnimalSerializer(animals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AnimalDetail(generics.RetrieveDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
