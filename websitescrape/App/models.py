from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=250)
    price = models.CharField(max_length=100)
    product_description = models.TextField()