from django.contrib import admin
from .models import Session
from .models import Shot

# Register your models here.
admin.site.register(Session)
admin.site.register(Shot)