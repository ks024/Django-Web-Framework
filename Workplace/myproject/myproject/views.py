from django.http import HttpResponse

def handler404(request, exception):
    return HttpResponse("<h1>404: Page Not Found!</h1>")

def home(request):
    return HttpResponse("<h1> Little Lemon Home Page! </h1>")