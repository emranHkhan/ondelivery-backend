from rest_framework import serializers
from .models import Review, FoodItem

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    food_item = serializers.PrimaryKeyRelatedField(queryset=FoodItem.objects.all())

    class Meta:
        model = Review
        fields = ['id', 'user', 'food_item', 'rating', 'comment', 'created_at', 'updated_at']
