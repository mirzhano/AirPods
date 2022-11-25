from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Pods(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    cost = models.IntegerField()
    characteristic = models.TextField(null=True)

class Characteristic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    image3 = models.ImageField(upload_to='')
    cost = models.IntegerField()
    characteristic = models.TextField(null=True)

class About_us(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    image3 = models.ImageField(upload_to='')
    characteristic = models.TextField(null=True)


    def __str__(self):
        return self.title