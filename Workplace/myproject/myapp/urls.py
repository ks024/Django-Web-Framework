from django.urls import path
from . import views

urlpatterns = [
    path('drink/<str:drink_name>', views.drinks, name='drinks')
]
