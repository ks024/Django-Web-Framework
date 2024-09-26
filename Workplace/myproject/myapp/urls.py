from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.form_view, name='home'),
    path('model/', views.model_form_view, name='model_form'),
    path('drink/<str:drink_name>', views.drinks, name='drinks')
]
