from django.urls import path
from . import views
from .views import EmployeeDelete, EmployeeUpdate, NewView, IndexView, EmployeeCreate, EmployeeList, EmployeeDetail

urlpatterns = [
    path('home/', views.form_view, name='home'),
    path('model/', views.model_form_view, name='model_form'),
    path('drink/<str:drink_name>', views.drinks, name='drinks'),
    path('about/', NewView.as_view()),
    path('new-file/', IndexView.as_view(), name='new_file'),
    path('create/', EmployeeCreate.as_view(), name = 'EmployeeCreate'),
    path('list/', EmployeeList.as_view(), name='employee_list'),
    path('show/<int:pk>', EmployeeDetail.as_view(), name = 'EmployeeDetail'),
    path('update/<int:pk>', EmployeeUpdate.as_view(), name = 'EmployeeUpdate'),
    path('delete/<int:pk>', EmployeeDelete.as_view(), name = 'EmployeeDelete') 
]
