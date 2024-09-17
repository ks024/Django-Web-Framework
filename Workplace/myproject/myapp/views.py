from django.http import HttpResponse

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
