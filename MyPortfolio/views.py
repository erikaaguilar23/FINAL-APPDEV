
from django.shortcuts import render
from .models import Project  # Import any models you need

def base(request):
    # Logic for base page (if any)
    return render(request, 'portfolio/index.html')
# Compare this snippet from portfolio_project/portfolio/templates/portfolio/home.html:

