from django.db import models


class KeyWord(models.Model):
    name = models.CharField(max_length=100,unique=True)



class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Shop(User):
    shop_name = models.CharField(max_length=200)
    loction_latitude = models.CharField(max_length=100)
    loction_longitude = models.CharField(max_length=100)

class Product(models.Model):
    image = models.ImageField(upload_to='product_images/')
    name = models.CharField(max_length=100,null=True)
    price = models.IntegerField(null=True)
    keywords = models.ManyToManyField(KeyWord)
    shop = models.ForeignKey(Shop)



class Customer(User):
    pass


# Create your models here.
