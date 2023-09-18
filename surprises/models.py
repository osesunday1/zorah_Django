from django.db import models
from django.urls import reverse

# Create your models here.

class Surprises(models.Model):
    surprise_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    sur_image = models.ImageField(upload_to='photos/surprises', blank=True)


    def get_url(self):
            return reverse('products_by_surprises', args=[self.slug])
    

    def __str__(self):
        return self.surprise_name