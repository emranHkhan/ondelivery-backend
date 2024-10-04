from django.urls import path
from .views import RestaurantListCreateView

urlpatterns = [
    path('restaurants/', RestaurantListCreateView.as_view(), name='restaurant-list-create'),
]