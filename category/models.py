from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) 
    image_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name
