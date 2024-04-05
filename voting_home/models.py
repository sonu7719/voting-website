from django.db import models

# Create your models here.
class Feedback(models.Model):
    Sr_no =models.AutoField(primary_key=True)
    First_name =models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    Content=models.CharField(max_length=200)
    
