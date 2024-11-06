from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from core.models import SoftDeleteModel
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    """
    Custom user manager where email is the unique identifier
    for authentication instead of usernames.
    """
    
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a regular User with the given email and password.
        
        Args:
            email: User's email address (used as identifier)
            password: User's password
            **extra_fields: Additional fields like first_name, last_name etc.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser, SoftDeleteModel):
    USER_TYPES = [
        ('free', 'Free User'),
        ('paid', 'Paid User'),
        ('admin', 'Admin User'),
    ]

    PREFERRED_UNITS = [
        ('yards', 'Yards'),
        ('metres', 'Metres'),
    ]

    username = None
    email = models.EmailField('Email Address', unique=True)
    first_name = models.CharField('First Name', max_length=150)
    last_name = models.CharField('Last Name', max_length=150)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='paid')
    has_paid = models.BooleanField(default=True)
    preferred_units = models.CharField(max_length=6, choices=PREFERRED_UNITS, default='yards')
    handicap = models.FloatField(null=True, blank=True)
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email