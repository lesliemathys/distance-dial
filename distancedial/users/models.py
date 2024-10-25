from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models

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
       # Normalize email address (lowercase the domain part)
       email = self.normalize_email(email)
       
       # Create new user instance but don't save to db yet
       user = self.model(email=email, **extra_fields)
       
       # Hash the password and set it
       user.set_password(password)
       
       # Save the user to the database
       user.save()
       return user

   def create_superuser(self, email, password, **extra_fields):
       """
       Create and save a SuperUser with the given email and password.
       
       SuperUsers are automatically given all permissions:
       - is_staff: Can access admin panel
       - is_superuser: Has all permissions
       - is_active: Account is active
       """
       # Set default admin privileges
       extra_fields.setdefault('is_staff', True)
       extra_fields.setdefault('is_superuser', True)
       extra_fields.setdefault('is_active', True)
       
       # Use the create_user method to create and save the superuser
       return self.create_user(email, password, **extra_fields)

# Create your models here.
class User(AbstractUser):

    # We've got a free user type to assist with me getting people to use and test the app
    USER_TYPES = [
        ('free', 'Free User'),
        ('paid', 'Paid User'),
        ('admin', 'Admin User'),
    ]

    PREFERRED_UNITS = [
        ('yards', 'Yards'),
        ('metres', 'Metres'),
    ]

    # We are using email as username, so are overriding the username field
    username = None
    email = models.EmailField('Email Address', unique=True)

    first_name = models.CharField('First Name', max_length=150)
    last_name = models.CharField('Last Name', max_length=150)

    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='paid')

    # Defaulting to true because user comes in via marketing site only, so in theory has to have paid
    has_paid = models.BooleanField(default=True) 

    preferred_units = models.CharField(max_length=6, choices=PREFERRED_UNITS, default='yards')

    handicap = models.FloatField(null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()


    def __str__(self):
        return self.email
