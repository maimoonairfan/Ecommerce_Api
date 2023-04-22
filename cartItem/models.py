from django.db import models
from cart.models import Cart
from products.models import Product

# Create your models here.
class CartItem(models.Model):
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    cartid = models.ForeignKey(Cart,on_delete=models.CASCADE,default=True)
    productid = models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str___(self):
        return self.quantity