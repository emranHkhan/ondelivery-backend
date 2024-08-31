from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    ingredients = models.JSONField()  # You can use ArrayField if using PostgreSQL
    image_url = models.URLField(max_length=500)
    ratings = models.DecimalField(max_digits=3, decimal_places=2)
    tags = models.JSONField()  # Or ArrayField for PostgreSQL
    dietary_info = models.JSONField()  # Or ArrayField for PostgreSQL

    def __str__(self):
        return self.name
