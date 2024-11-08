from django.urls import path
from .views import LandingPageView

app_name = 'marketing_site'

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
]