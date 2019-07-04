from django.shortcuts import render


def home(request):
    """information home page"""

    return render(request, 'home.html')

def about(request):
    """about me """

    return render(request, 'about.html')