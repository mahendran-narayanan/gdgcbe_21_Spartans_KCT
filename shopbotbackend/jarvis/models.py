from django.db import models


class KeyWord(models.Model):
    name = models.CharField(max_length=100,unique=True)

class Product(models.Model):
    image = models.ImageField(upload_to='product_images/')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    keywords = models.ManyToManyField(KeyWord)


class ShopOwner(models.Model):
    name = models.CharField(max_length=200)


# Create your models here.
