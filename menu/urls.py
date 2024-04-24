from django.urls import path
from . import views

urlpatterns = [
    path('', views.MealsListView.as_view(), name='meals'),
    path('<int:meal_id>', views.SpecificMealView.as_view(), name='meal')
]