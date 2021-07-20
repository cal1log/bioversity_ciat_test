from rest_framework import generics
from .models import Animals, Deforestations
from .serializers import AnimalsSerializer, DeforestationsSerializer

class AnimalsAPIView(generics.ListCreateAPIView):
    queryset = Animals.objects.all()
    serializer_class = AnimalsSerializer

class DeforestationsAPIView(generics.ListCreateAPIView):
    queryset = Deforestations.objects.all()
    serializer_class = DeforestationsSerializer


