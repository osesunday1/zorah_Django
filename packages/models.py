from django.db import models
from django.urls import reverse

# Create your models here.

class Packages(models.Model):
    package_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    pac_image = models.ImageField(upload_to='photos/packages', blank=True)


    def get_url(self):
            return reverse('products_by_packages', args=[self.slug])
    

    def __str__(self):
        return self.package_name