from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['email', 'first_name', 'last_name']  # Search by email or name
    list_display = ['email', 'first_name', 'last_name', 'user_type', 'has_paid']  # Columns shown in list view
    list_filter = ['user_type', 'has_paid', 'preferred_units']  # Filters shown on right side