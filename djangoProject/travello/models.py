from django.db import models

# Create your models here.

class Destination:
    id : int
    name : str
    img : str
    descp : str
    price : int