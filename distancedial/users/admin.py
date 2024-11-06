from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['email', 'first_name', 'last_name']
    list_display = ['email', 'first_name', 'last_name', 'user_type', 'has_paid', 'is_deleted']
    list_filter = ['user_type', 'has_paid', 'preferred_units', 'is_deleted']
    list_per_page = 25
    
    def get_queryset(self, request):
        # Show all objects, including soft-deleted ones
        return self.model.all_objects.all()