from .models import Meal
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from . import serializers

# Create your views here.

class MealsListView(generics.GenericAPIView):

    serializer_class = serializers.MealsListSerializer
    queryset = Meal.objects.all()

    def get(self, request):

        meals = Meal.objects.all()

        serializer = self.serializer_class(instance=meals, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
class SpecificMealView(generics.GenericAPIView):

    serializer_class = serializers.SpecificMealSerializer

    def get(self, request, meal_id):

        meal = get_object_or_404(Meal, pk=meal_id)

        serializer = self.serializer_class(instance=meal)

        return Response(data=serializer.data, status=status.HTTP_200_OK)