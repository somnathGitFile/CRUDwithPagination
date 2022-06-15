from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    customer_email =models.EmailField()
    customer_address=models.CharField(max_length=100)
    customer_pan =models.CharField(max_length=50)
    customer_adhar=models.IntegerField()
