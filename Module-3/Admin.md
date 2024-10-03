# Django Admin and User Management Overview

## Table of Contents

1. **[Introduction to Django Admin](#1-introduction-to-django-admin)**
2. **[Setting Up Django Admin](#2-setting-up-django-admin)**
   - [2.1 Enabling the Admin Interface](#21-enabling-the-admin-interface)
   - [2.2 Creating a Superuser](#22-creating-a-superuser)
   - [2.3 Accessing the Admin Interface](#23-accessing-the-admin-interface)
3. **[Using the Admin Interface](#3-using-the-admin-interface)**
4. **[User Management in Django Admin](#4-user-management-in-django-admin)**
   - [4.1 User Roles](#41-user-roles)
   - [4.2 Permissions System](#42-permissions-system)
   - [4.3 Managing User Permissions](#43-managing-user-permissions)
     - [4.3.1 Using the Admin Interface](#431-using-the-admin-interface)
     - [4.3.2 Programmatically](#432-programmatically)
   - [4.4 Groups and User Management](#44-groups-and-user-management)
     - [4.4.1 Creating Groups](#441-creating-groups)
     - [4.4.2 Assigning Users to Groups](#442-assigning-users-to-groups)
5. **[Customizing the User Admin](#5-customizing-the-user-admin)**
   - [5.1 Unregistering and Registering User Admin](#51-unregistering-and-registering-user-admin)
   - [5.2 Conditional Field Accessibility](#52-conditional-field-accessibility)
6. **[Defining Models and Registering with Admin](#6-defining-models-and-registering-with-admin)**
7. **[Enforcing Permissions in Views](#7-enforcing-permissions-in-views)**
   - [7.1 Basic Permission Checks](#71-basic-permission-checks)
   - [7.2 Using Decorators](#72-using-decorators)
   - [7.3 Class-Based Views](#73-class-based-views)
   - [7.4 Enforcing Permissions in Templates](#74-enforcing-permissions-in-templates)
8. **[Conclusion](#8-conclusion)**
9. **[Additional Resources](#9-additional-resources)**

---

## 1. Introduction to Django Admin

The Django admin interface is a powerful tool for managing application data, allowing users to perform CRUD (Create, Read, Update, Delete) operations, manage users, and configure permissions easily.

## 2. Setting Up Django Admin

### 2.1 Enabling the Admin Interface

To set up the Django admin, include `django.contrib.admin` in your `INSTALLED_APPS` in `settings.py`:

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

Create a superuser for managing the admin interface:

```bash
python3 manage.py createsuperuser
```

Follow the prompts to enter your username, email, and password.

### 2.3 Accessing the Admin Interface

Start the server:

```bash
python3 manage.py runserver
```

Navigate to `http://127.0.0.1:8000/admin` in your web browser and log in with your superuser credentials.

## 3. Using the Admin Interface

After logging in, you can manage users, groups, and models. The interface provides easy options for adding, changing, and deleting entries.

## 4. User Management in Django Admin

### 4.1 User Roles

Django recognizes several user roles:

- **Superuser**: Full access to all features.
- **Staff User**: Can access the admin interface with granted permissions.
- **Regular User**: No default access to the admin interface.

### 4.2 Permissions System

Permissions dictate what actions users can perform. Each model has permissions created with the format `app_label.action_model`. For example:

- `myapp.add_mymodel`
- `myapp.change_mymodel`
- `myapp.delete_mymodel`
- `myapp.view_mymodel`

### 4.3 Managing User Permissions

You can assign permissions to users and groups through the admin interface or programmatically.

#### 4.3.1 Using the Admin Interface

1. Navigate to the **Users** section.
2. Click on a user to edit and adjust their permissions.

#### 4.3.2 Programmatically

Manage user permissions using Django's User model:

```python
from django.contrib.auth.models import User, Permission

# Create a user
user = User.objects.create_user(username='new_user', password='password123')

# Assign a permission
permission = Permission.objects.get(codename='change_mymodel', content_type__app_label='myapp')
user.user_permissions.add(permission)
```

### 4.4 Groups and User Management

Groups help manage permissions collectively.

#### 4.4.1 Creating Groups

1. Navigate to the **Groups** section in the admin panel.
2. Click **Add Group** to create a new group and assign permissions.

#### 4.4.2 Assigning Users to Groups

Add users to groups either in the admin interface or programmatically:

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

Then create a custom User admin class:

```python
from django.contrib.auth.admin import UserAdmin

@admin.register(User)
class NewUserAdmin(UserAdmin):
    readonly_fields = ['date_joined']  # Example of making a field read-only
```

### 5.2 Conditional Field Accessibility

Restrict access to specific fields based on user roles:

```python
def get_form(self, request, obj=None, **kwargs):
    form = super().get_form(request, obj, **kwargs)
    if not request.user.is_superuser:
        form.base_fields['username'].disabled = True
    return form
```

## 6. Defining Models and Registering with Admin

Define new models in `models.py`:

```python
from django.db import models

class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
```

Register the model in `admin.py`:

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

Enforce permissions at the view level using decorators:

```python
from django.core.exceptions import PermissionDenied

def myview(request):
    if not request.user.has_perm('myapp.change_mymodel'):
        raise PermissionDenied()
```

### 7.2 Using Decorators

Use `@login_required` and `@permission_required` decorators for permission checks:

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

Check permissions directly in templates:

```django
{% if user.has_perm('myapp.change_mymodel') %}
    <a href="{% url 'change_model_view' %}">Change Model</a>
{% endif %}
```

## 8. Conclusion

Django's admin interface, combined with its user and permission management systems, provides an efficient way to manage data and control access. By following the outlined steps, you can configure the admin interface, customize user management, and enforce permissions effectively.

## 9. Additional Resources

- [Django Admin and manage.py – official documentation](https://docs.djangoproject.com/en/4.1/ref/django-admin/)
- [Using the Django authentication system](https://docs.djangoproject.com/en/4.1/topics/auth/default/)
- [Django Admin site – MDN web docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site)
- [Django Admin-site – Comprehensive](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/)
- [Django permissions – TestDriven](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/)
``
