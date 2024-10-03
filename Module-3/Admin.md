# Django Admin and User Management Overview

## 1. Introduction to Django Admin

The Django admin interface is a powerful tool that simplifies the management of application data. It provides an intuitive way to perform CRUD (Create, Read, Update, Delete) operations, manage users, and configure permissions.

## 2. Setting Up Django Admin

### 2.1 Enabling the Admin Interface

To set up the Django admin, ensure that `django.contrib.admin` is included in your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp.apps.MyappConfig',  # Your custom app
]
```

### 2.2 Creating a Superuser

To manage the admin interface, create a superuser by running:

```bash
python3 manage.py createsuperuser
```

Follow the prompts to enter your username, email, and password.

### 2.3 Accessing the Admin Interface

Start the server:

```bash
python3 manage.py runserver
```

Navigate to `http://127.0.0.1:8000/admin` in your web browser to log in with your superuser credentials.

## 3. Using the Admin Interface

After logging in, you can manage users, groups, and your models. The interface allows for adding, changing, and deleting entries easily.

## 4. User Management in Django Admin

### 4.1 User Roles

Django distinguishes between several user roles:

- **Superuser**: Has full access to all features.
- **Staff User**: Can access the admin interface with granted permissions.
- **Regular User**: By default, has no access to the admin interface.

### 4.2 Permissions System

Permissions control what actions users can perform. Permissions are automatically created for each model with the naming convention `app_label.action_model`. For example, for a model `my_model` in an app `myapp`:

- `myapp.add_mymodel`
- `myapp.change_mymodel`
- `myapp.delete_mymodel`
- `myapp.view_mymodel`

### 4.3 Managing User Permissions

You can assign permissions to users and groups in the Django admin interface or programmatically.

#### Using the Admin Interface

1. Navigate to the **Users** section.
2. Click on a user to edit and adjust their permissions in the permissions section.

#### Programmatically

You can manage user permissions using Django's User model:

```python
from django.contrib.auth.models import User, Permission

# Create a user
user = User.objects.create_user(username='new_user', password='password123')

# Assign a permission
permission = Permission.objects.get(codename='change_mymodel', content_type__app_label='myapp')
user.user_permissions.add(permission)
```

### 4.4 Groups and User Management

Groups help manage permissions collectively:

#### Creating Groups

1. Navigate to the **Groups** section in the admin panel.
2. Click **Add Group** to create a new group and assign permissions.

#### Assigning Users to Groups

You can add users to groups in the admin interface or programmatically:

```python
from django.contrib.auth.models import Group

group = Group.objects.create(name='Staff')
user.groups.add(group)  # Add user to group
```

## 5. Customizing the User Admin

### 5.1 Unregistering and Registering User Admin

To customize user management, unregister the default User admin:

```python
from django.contrib import admin
from django.contrib.auth.models import User

admin.site.unregister(User)
```

Then, create a custom User admin class:

```python
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class NewUserAdmin(UserAdmin):
    readonly_fields = ['date_joined']  # Example of making a field read-only
```

### 5.2 Conditional Field Accessibility

You can restrict access to specific fields based on user roles:

```python
def get_form(self, request, obj=None, **kwargs):
    form = super().get_form(request, obj, **kwargs)
    if not request.user.is_superuser:
        form.base_fields['username'].disabled = True
    return form
```

## 6. Defining Models and Registering with Admin

To define new models, create them in `models.py`:

```python
from django.db import models

class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
```

Then, register the model in `admin.py`:

```python
from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
    search_fields = ("first_name__startswith",)
```

## 7. Enforcing Permissions in Views

### 7.1 Basic Permission Checks

You can enforce permissions at the view level using decorators:

```python
from django.core.exceptions import PermissionDenied

def myview(request):
    if not request.user.has_perm('myapp.change_mymodel'):
        raise PermissionDenied()
```

### 7.2 Using Decorators

Use `@login_required` and `@permission_required` decorators for simple permission checks:

```python
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def myview(request):
    return HttpResponse("Hello World")

@permission_required("myapp.change_mymodel")
def change_model_view(request):
    # Logic for changing the model
```

### 7.3 Class-Based Views

For class-based views, use `PermissionRequiredMixin`:

```python
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

class MyModelListView(PermissionRequiredMixin, ListView):
    permission_required = "myapp.view_mymodel"
    model = MyModel
    template_name = "mymodel_list.html"
```

### 7.4 Enforcing Permissions in Templates

You can check permissions directly in templates:

```django
{% if user.has_perm('myapp.change_mymodel') %}
    <a href="{% url 'change_model_view' %}">Change Model</a>
{% endif %}
```

## 8. Conclusion

Django's admin interface, along with its robust user and permission management systems, provides a streamlined way to manage data and control access in your applications. By following the steps outlined above, you can effectively configure the admin interface, customize user management, and enforce permissions across your Django project. This ensures a secure and efficient application environment tailored to your needs.
