from django.shortcuts import render

# views.py

# Add this cats list below the imports
finches = [
  {'name': 'Eduardo','species': 'house finch', 'true_finch': True, 'description': 'cute lil red and gray finch', 'length': 13, 'wingspan': 22},
  {'name': 'Indy Trunco','species': 'dark-eyed junco', 'true_finch': False, 'description': 'dark eyes, like the night', 'length': 14, 'wingspan': 14},
]



# Create your views here.
def home(request):
    # Define the home view
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })