
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('marketing_site.urls')),  # Root URL for marketing site

]
