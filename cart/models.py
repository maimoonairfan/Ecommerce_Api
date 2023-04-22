from django.db import models
# Create your models here.
class Cart(models.Model):
    totalprice = models.IntegerField(default=0)
    def __str___(self):
        return self.totalprice
    
