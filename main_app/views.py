from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class FinchCreate(CreateView):
    model = Finch
    # The fields attribute if required for a create view
    fields = '__all__'
    # Same as below =>
    # fields = ['name', 'species', 'true_finch', 'description', 'length', 'wingspan']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['description']

class FinchDelete(DeleteView):
    model = Finch
    #success url, index page
    success_url = '/finches/'