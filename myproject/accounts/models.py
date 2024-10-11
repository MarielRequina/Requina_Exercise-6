# models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Add any required fields here

    def __str__(self):
        return self.email

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
