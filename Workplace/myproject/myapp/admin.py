from django.contrib import admin
from .models import Person, Logger

# Register your models here.
admin.site.register(Person)
admin.site.register(Logger)