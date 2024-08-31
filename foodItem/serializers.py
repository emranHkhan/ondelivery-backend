from rest_framework import serializers
from .models import FoodItem

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = [
            'id', 'name', 'description', 'price', 'category', 'availability',
            'ingredients', 'image_url', 'ratings', 'tags', 'dietary_info'
        ]
