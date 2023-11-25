from django.db import models

# Create your models here.
class auction(models.Model):
    img = models.TextField()
    descraption = models.TextField()
    price = models.TextField()

class truck_part(models.Model):
    img = models.TextField()
    descraption = models.TextField()
    price = models.TextField()
    