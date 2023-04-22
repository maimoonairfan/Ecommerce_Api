from django.db import models
# Create your models here.
class Authority(models.Model):

    emailid = models.CharField(max_length = 1000)
    authorities = models.CharField(max_length = 1000)
    

    def __str___(self):
        return self.emailid