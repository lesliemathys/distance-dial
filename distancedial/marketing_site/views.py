from django.shortcuts import render
from django.views.generic import TemplateView

class LandingPageView(TemplateView):
    template_name = "pages/index.html"

def home(request):
    return render(request, 'pages/index.html')