from django.shortcuts import render
from rest_framework import generics
from .serializers import Food, FoodSerializer
# Create your views here.

class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all().order_by('id')
    serializer_class = FoodSerializer

class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all().order_by('id')
    serializer_class = FoodSerializer