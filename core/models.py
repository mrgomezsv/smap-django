from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.IntegerField()
    featured_image = models.CharField(max_length=255)
    description = models.TextField()
    additional_images = models.JSONField()
