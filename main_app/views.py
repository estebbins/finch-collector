from django.shortcuts import render, redirect
from .models import Finch, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .forms import FeedingForm
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
    # Get the toys the finch doesn't have...
    # First, create a list of the toy ids that the finch DOES have
    id_list = finch.toys.all().values_list('id')
    # Now we can query for toys whose ids are not in the list using exclude
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
        'finch': finch, 'feeding_form': feeding_form,
        # Add the toys to be displayed
        'toys': toys_finch_doesnt_have
    })

def add_feeding(request, finch_id):
    # Create a model form instance form the data in request.POST
    form = FeedingForm(request.POST)
    # Validate form (does it match our data)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
    model = Finch
    # The fields attribute if required for a create view
    # Same as below =>
    fields = ['name', 'species', 'true_finch', 'description', 'length', 'wingspan', 'picture']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['description']

class FinchDelete(DeleteView):
    model = Finch
    #success url, index page
    success_url = '/finches/'


# ToyList
class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'

# ToyDetail
class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'
# ToyCreate
class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']

    # define what the inherited method is_valid does (we'll update this later)
    def form_valid(self, form):
        #use later, implement now
        #we'll need this when we add auth
        #Super allows for the original inherited CreateView function to work as it was intended
        return super().form_valid(form)
# ToyUpdate
class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

# ToyDelete
class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

def assoc_toy(request, finch_id, toy_id):
    # Note that you can pass a toy's id instead of the whole toy object
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.remove(toy_id)
    return redirect('detail', finch_id=finch_id)