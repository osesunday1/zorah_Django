from django.db import models
from category.models import Category
from packages.models import Packages
from surprises.models import Surprises
from django.urls import reverse
from accounts.models import Account
from django.db.models import Avg, Count

# Create your models here.

class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, null=True,  blank= True)
    packages        = models.ForeignKey(Packages, on_delete=models.CASCADE, default=None, null=True, blank= True)
    surprises       = models.ForeignKey(Surprises, on_delete=models.CASCADE, default=None, null=True,  blank= True)    
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return self.product_name