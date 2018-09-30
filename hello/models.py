from django.db import models
from cloudinary import models as cloud_models


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class Product(models.Model):
    image = cloud_models.CloudinaryField('image')