from django.db import models

# Create your models here.



# class  vote(models.Model):
#     Adhar_no=models.BigIntegerField(primary_key=True)
#     First_Name=models.CharField(max_length=100)
#     Last_name=models.CharField(max_length=100)
#     Address=models.CharField(max_length=200)
class vote(models.Model):
    First_name=models.CharField(max_length=100)
    Age=models.CharField(max_length=100)

    party = models.CharField(max_length=50)

class cal_votes(models.Model):
    party = models.CharField(max_length=50)
    n_vote = models.IntegerField(default = 0)

    
    



  


