from rest_framework import serializers
from .models import FoodItem
from review.models import Review
from review.serializers import ReviewSerializer
from restaurant.serializers import RestaurantSerializer
from django.db.models import Avg
from math import ceil  
class FoodItemSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    restaurants = RestaurantSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField() 
    class Meta:
        model = FoodItem
        fields = ['id', 'name', 'description', 'price', 'availability', 'ingredients', 'category', 'image_url', 'tags', 'dietary_info', 'restaurants', 'reviews', 'average_rating']

    def get_average_rating(self, obj):
        avg_rating = Review.objects.filter(food_item=obj).aggregate(Avg('rating'))['rating__avg']

        if avg_rating is None:
            return 0
        
        return ceil(avg_rating) 
    