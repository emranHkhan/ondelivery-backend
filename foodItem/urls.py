from django.urls import path
from .views import FoodItemDetailView, FoodItemListView

urlpatterns = [
    path('fooditems/', FoodItemListView.as_view(), name='fooditem-create'),
    path('fooditems/<int:pk>/', FoodItemDetailView.as_view(), name='fooditem-detail'),
]
