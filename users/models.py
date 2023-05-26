from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    # by default django want's to login with username + password
    REQUIRED_FIELDS = ['password', 'username']


#todo -- check requiredFields in the doc (for me those fields are ok)
