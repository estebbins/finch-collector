from django.shortcuts import render
from .models import Finch

# views.py

# Seed data
# finches = [
#   {'name': 'Eduardo','species': 'house finch', 'true_finch': True, 'description': 'cute lil red and gray finch', 'length': 13, 'wingspan': 22},
#   {'name': 'Indy Trunco','species': 'dark-eyed junco', 'true_finch': False, 'description': 'dark eyes, like the night', 'length': 14, 'wingspan': 14},
# ]

# Create your views here.
def home(request):
    # Define the home view
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', { 'finch': finch })