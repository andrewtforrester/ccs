from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=127)
    price = models.IntegerField(default=0) #cents

    def __str__(self):
        return self.name