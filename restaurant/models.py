from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
