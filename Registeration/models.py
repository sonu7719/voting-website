from django.db import models
from django.forms import ValidationError

# Create your models here.

# class register(models.Model):
#     Adhar_no=models.BigIntegerField(primary_key=True)
#     First_Name=models.CharField(max_length=100)
#     Password=models.CharField(max_length=100)
#     confim_password=models.CharField(max_length=100,default='')
#     email_name=models.EmailField(max_length=200,default='')


# new model for the password verification
class Register(models.Model):
    Adhar_no = models.BigIntegerField(primary_key=True)
    First_Name = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Confirm_Password = models.CharField(max_length=100, default='')
    Email = models.EmailField(max_length=200, default='')

    def save(self, *args, **kwargs):
        if self.Password != self.Confirm_Password:
            raise ValidationError("Password and Confirm Password do not match.")
        super(Register, self).save(*args, **kwargs)
   
    
