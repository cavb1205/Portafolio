from django.shortcuts import render

def home(request):
    """information home page"""

    return render(request, 'home.html')