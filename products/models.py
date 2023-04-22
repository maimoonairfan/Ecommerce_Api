from django.db import models
# Create your models here.
class Product(models.Model):
    max_length = 255,
    category = models.CharField(max_length = 1000)
    description = models.CharField(max_length = 1000)
    name = models.CharField(max_length = 200)
    manufacturer = models.CharField(max_length = 500)
    price = models.IntegerField(default=0)
    unitprice = models.IntegerField(default=0)
    date_created = models.DateField(auto_created=True)
    last_modified = models.DateField(auto_now=True)

    def __str___(self):
        return self.name