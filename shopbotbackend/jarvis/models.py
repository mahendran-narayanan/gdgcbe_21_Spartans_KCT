from django.db import models


class KeyWord(models.Model):
    name = models.CharField(max_length=100,unique=True)

class Product(models.Model):
    image = models.ImageField(upload_to='product_images/')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    keywords = models.ManyToManyField(KeyWord)


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Shop(User):
    shop_name = models.CharField(max_length=200)
    loction_latitude = models.CharField(max_length=100)
    loction_longitude = models.CharField(max_length=100)

class Customer(User):
    pass


# Create your models here.
