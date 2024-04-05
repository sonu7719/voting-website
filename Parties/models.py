from django.db import models

# Create your models here.

class parties(models.Model):
    Partie_no=models.CharField(max_length=100)
    sponser=models.CharField(max_length=100)
    Party_name=models.CharField(max_length=100)
    Partie_Email=models.EmailField(max_length=200,default='')
    Leader=models.CharField(max_length=100)
    
