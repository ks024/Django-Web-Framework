from django.contrib import admin
from django.contrib.auth.admin import User
from .models import Person, Logger


# Register your models here.
admin.site.register(Person)
admin.site.register(Logger)

admin.site.unregister(User)


from django.contrib.auth.admin import UserAdmin

@admin.register(User) 
class NewAdmin(UserAdmin): 
    def get_form(self, request, obj=None, **kwargs): 
        form = super().get_form(request, obj, **kwargs) 
        is_superuser = request.user.is_superuser 

        if not is_superuser: 
            form.base_fields['username'].disabled = True 

        return form 