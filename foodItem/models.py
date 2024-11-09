from django.db import models
from restaurant.models import Restaurant
from category.models import Category

class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    availability = models.BooleanField(default=True)
    ingredients = models.JSONField()
    image_url = models.URLField(max_length=500)
    tags = models.JSONField()
    dietary_info = models.JSONField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='food_items')
    restaurants = models.ManyToManyField(Restaurant, related_name='food_items', blank=True)

    def __str__(self):
        return self.name