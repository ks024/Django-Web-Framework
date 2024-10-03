from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from myapp.forms import InputForm, LogForm
from myapp.models import Employee

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

def model_form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "model.html", context)


# Class Generic views

class NewView(View):   
    def get(self, request):   
        # View logic will place here   
        return HttpResponse('response') 
    
class IndexView(TemplateView): 
    template_name = 'new_file.html' 

class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    success_url = "/demo/create/"
    template_name = 'myapp/employeeCreate.html'


class EmployeeList(ListView):
    model = Employee
    success_url = "/employees/success/"
    template_name = 'myapp/employee_list.html'

class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'myapp/employee_detail.html'

from django.views.generic.edit import UpdateView  
class EmployeeUpdate(UpdateView):   
    model = Employee   
    fields = '__all__'   
    success_url = "/employees/success/" 
    template_name = 'myapp/employee_update_form.html'

from django.views.generic.edit import DeleteView 
class EmployeeDelete(DeleteView):   
    model = Employee   
    success_url = "/employees/success/"
    template_name = 'myapp/employee_confirm_delete.html'


    

