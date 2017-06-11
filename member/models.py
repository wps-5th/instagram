from django.db import models

# Create your models here.

class User(models.Model):
    user_ID = models.CharField(max_length=10)
    user_email = models.CharField(max_length=20)
