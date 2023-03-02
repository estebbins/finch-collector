from django.shortcuts import render

# Create your views here.
def home(request):
    # Define the home view
    return render(request, 'home.html')