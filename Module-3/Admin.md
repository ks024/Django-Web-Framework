# Django Admin Overview

## 1. Purpose

The Django admin interface enables site administrators to manage application data efficiently. It simplifies tasks like adding, editing, and deleting content, managing users, and controlling permissions.

## 2. Automatic Interface

Once you register your models in Django, the admin interface automatically generates forms for CRUD (Create, Read, Update, Delete) operations based on those models.

## 3. Setting Up

To set up the Django admin:

- Ensure `django.contrib.admin` is included in your `INSTALLED_APPS` in `settings.py`.
- Create a superuser by running:

  ```bash
  python3 manage.py createsuperuser
  ```

  Follow the prompts to input your username, email, and a strong password.

## 4. Accessing the Admin Interface

- Start the server with:

  ```bash
  python3 manage.py runserver
  ```

- Navigate to `http://127.0.0.1:8000/admin` in your web browser to access the admin interface.

## 5. Using the Interface

- Log in with your superuser credentials.
- Manage users, groups, and your models (e.g., reservations).
- Use the available options to add, change, and delete entries.

## 6. Permissions

You can assign specific permissions to users and groups, enabling granular control over actions they can perform.

### Benefits

Using the Django admin panel streamlines the development process, allowing you to focus on building features rather than creating admin tools from scratch. It is invaluable for quick data management and adjustments as you progress in your learning.

---

### Managing Users in Django Admin

#### 1. Django Admin Setup

Django provides a built-in admin interface via the `django.contrib.admin` app, which is included by default in your project’s `INSTALLED_APPS`. This interface allows efficient management of application data.

#### 2. User Permissions

- **User Roles**: Users require permissions to perform tasks. Permissions can be granted individually or through groups.
- **Staff Access**: A user must have `is_staff` set to `True` to log into the admin interface. Without appropriate permissions, users may have limited functionality.

#### 3. Customizing User Admin

To customize user management in Django Admin:

- **Unregister the Default User Admin**: To modify the default User admin, unregister it in your app’s `admin.py`:

  ```python
  from django.contrib import admin
  from django.contrib.auth.models import User
  
  admin.site.unregister(User)
  ```

- **Register a New User Admin**: Create a custom User admin class with the `@admin.register()` decorator, allowing you to customize user display and management:

  ```python
  from django.contrib.auth.admin import UserAdmin
  
  @admin.register(User)
  class NewAdmin(UserAdmin):
      pass
  ```

#### 4. Readonly Fields

To make certain fields non-editable (e.g., `date_joined`), specify them in the `readonly_fields` attribute:

```python
class NewAdmin(UserAdmin):
    readonly_fields = ['date_joined']
```

#### 5. Conditional Field Accessibility

To restrict access to specific fields (like `username`) based on user roles, override the `get_form()` method in your custom User admin class:

```python
def get_form(self, request, obj=None, **kwargs):
    form = super().get_form(request, obj, **kwargs)
    if not request.user.is_superuser:
        form.base_fields['username'].disabled = True
    return form
```

#### 6. Creating a New App

To extend your project with new models:

- Create a new Django app (e.g., `myapp`).
- Add this app to the `INSTALLED_APPS` list in `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp.apps.MyappConfig',
]
```

#### 7. Defining Models

Define your models in the `models.py` file within your new app. For example, a `Person` model can be defined as follows:

```python
from django.db import models

class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
```

#### 8. Registering Models in Admin

To make the `Person` model available in the admin interface, register it:

```python
from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
    search_fields = ("first_name__startswith",)
```

#### 9. Admin Interface Customization

- **Display Attributes**: The `list_display` attribute in the `PersonAdmin` class specifies which fields are shown in the list view of the admin interface for clarity.
  
- **Search Functionality**: The `search_fields` attribute allows enabling a search box in the admin interface to filter results based on specified fields (e.g., first names starting with a certain letter).

### Conclusion

By following these steps, you can effectively manage users and customize the Django Admin interface to meet your project’s needs. You have learned to handle user permissions carefully, customize user management, create new models, and enhance the admin experience. This improves both the security and usability of the admin interface.
