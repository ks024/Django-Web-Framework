from django.http import HttpResponse
from django.shortcuts import render
from myapp.forms import InputForm

# Create your views here.
def drinks(request, drink_name):
    # Dictionary of drink types
    drink = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment',
    }
    
    # Get the description of the drink using drink_name
    choice_of_drink = drink[drink_name]
    
    # Return an HTTP response with the drink name and description
    return HttpResponse(f"<h2>{drink_name}</h2><p>{choice_of_drink}</p>")

def home(request):
    return HttpResponse("HomePage")

def form_view(request):
    form = InputForm()
    context = {"form": form}
    return render(request, "home.html", context)

