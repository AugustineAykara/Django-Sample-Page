from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    descp = models.TextField()
    price = models.IntegerField()
    specialOffer = models.BooleanField(default=False)