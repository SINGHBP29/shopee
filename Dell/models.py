from django.db import models
from django.forms import ModelForm

# Create your models here.

class Login(models.Model):
    Username = models.EmailField(max_length=90)
    Password1 = models.CharField(max_length=78)

'''class loginForm(ModelForm):
    Email = models.EmailField(max_length=63)'''
    
      

class registrationForm(models.Model):
    First_Name = models.CharField(max_length=45,null=True)
    username = models.EmailField(max_length=43,null=True)
    Password = models.CharField(max_length=78,null=True)
    password1 = models.CharField(max_length=78,null=True)