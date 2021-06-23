from django.db import models

# Create your models here.
class Product(models.Model):
    pid         = models.CharField(max_length=120)
    title       = models.CharField(max_length=120) # max_length is required
    description = models.TextField(blank= True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(null=True)
    featured    = models.BooleanField()