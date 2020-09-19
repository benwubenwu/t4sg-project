from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class CustomUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE) # also delete objs that have reference to it
#     bio = models.CharField(max_length=300, blank=True)

class NewUser(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100, unique=True)
    password = models.CharField(max_length = 100)
    bio = models.TextField(max_length = 300)