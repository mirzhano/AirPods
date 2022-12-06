from django.db import models

# Create your models here.
class Cat(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    cost = models.IntegerField()
    characteristic = models.TextField(null=True)


    def __str__(self):
        return self.title
