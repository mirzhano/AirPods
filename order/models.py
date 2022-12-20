from django.db import models

# Create your models here.
class Series(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    cost = models.IntegerField()
    characteristic = models.TextField(null=True)

class Order(models.Model):
    objects = None
    product = models.CharField(max_length=50,null=True)
    name = models.CharField(max_length=100)
    contact_number= models.IntegerField()
    adress= models.TextField()
    comment=models.TextField()
    email=models.EmailField()