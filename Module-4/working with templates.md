# Notes on Django Template Language (DTL)

## Table of Contents

1. [Overview](#overview)
2. [Key Benefits of DTL](#key-benefits-of-dtl)
3. [Main Constructs of DTL](#main-constructs-of-dtl)
   - [Variables](#variables)
   - [Tags](#tags)
   - [Filters](#filters)
   - [Comments](#comments)
4. [Using Templates in Django for Dynamic Web Pages](#using-templates-in-django-for-dynamic-web-pages)
5. [Creating a Dynamic Menu in Django](#creating-a-dynamic-menu-in-django)
6. [Understanding Template Inheritance in Django](#understanding-template-inheritance-in-django)
7. [Template Inheritance and Static Files in Django](#template-inheritance-and-static-files-in-django)
8. [Template Inheritance: Using Extends and Include Tags](#template-inheritance-using-extends-and-include-tags)

---

## Overview

Django Template Language (DTL) is essential for adding dynamic data inside HTML markup in web applications. It allows developers to separate presentation from application logic, facilitating a clean structure and improved maintainability.

## Key Benefits of DTL

- **Flexibility**: Based on the Jinja2 template engine, DTL aligns with familiar programming paradigms, making it easier for developers.
- **DRY Principle**: Promotes the "Don't Repeat Yourself" approach, which is a core principle in Django development.
- **Security**: The Python interpreter does not execute the template code, adding a layer of security.

## Main Constructs of DTL

### Variables

- **Syntax**: Enclosed in double curly braces `{{ variable }}`.
- **Functionality**: Evaluates and replaces the variable with the corresponding value.
- **Example**:

  ```html
  <h1>Welcome to {{ restaurant_name }}</h1>
  ```

  If `restaurant_name` is "Little Lemon", it renders: "Welcome to Little Lemon".

- **Lookup Options**: Supports dictionary, attribute, and list index lookup using dot notation.

  ```html
  {{ user.first_name }}
  {{ item_list.0.name }}
  ```

### Tags

- **Syntax**: Created using curly braces with percentage symbols `{% tag %}`.
- **Functionality**: Introduce logic into templates.
- **Common Tags**:
  - **Control Structures**: `if`, `for`
  - **If Tag Example**:

    ```django
    {% if logged_in %}
        <p>Welcome back, {{ user.username }}!</p>
    {% else %}
        <a href="/login">Login</a>
    {% endif %}
    ```

  - **For Loop Example**: Iterating over a menu list.

    ```django
    <ul>
    {% for item in menu_items %}
        <li>{{ item.name }} - ${{ item.price }}</li>
    {% endfor %}
    </ul>
    ```

### Filters

- **Functionality**: Modify the values of variables.
- **Syntax**: Applied using the pipe symbol `|`.
- **Examples**:
  - Uppercase conversion:

    ```django
    {{ name | upper }}  <!-- Outputs: JOHN DOE -->
    ```

  - Date formatting:

    ```django
    {{ my_date | date:"Y-m-d" }}  <!-- Outputs: 2023-10-03 -->
    ```

### Comments

- **Syntax**: Use `{# comment #}`.
- **Functionality**: Comments are ignored by Django and do not render in the output. Used for documentation purposes.

  ```django
  {# This is a comment and will not appear in the output #}
  ```

## Using Templates in Django for Dynamic Web Pages

### Step-by-Step Guide

1. **Setting Up Your Django App**:
   Locate `views.py` in your Django app's main directory.

2. **Creating the View Function**:
   Define a view function that takes the request object as a parameter.

   ```python
   from django.shortcuts import render

   def menu(request):
       menu_item = {'name': 'Greek Salad'}
       return render(request, 'menu.html', menu_item)
   ```

3. **Creating the Template**:
   Create a folder named `templates`, and inside it, create `menu.html`.

4. **Writing the Template Code**:

   ```html
   <h2>Menu Item: {{ name }}</h2>
   ```

5. **Configuring Your Project**:
   Add the `templates` folder to the `TEMPLATES` list in `settings.py`.

6. **Setting Up URL Patterns**:
   In `urls.py`, map the URL to your view function:

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('menu/', views.menu, name='menu'),
   ]
   ```

7. **Running the Server**:
   Run your Django server and navigate to `http://localhost:8000/menu/`.

8. **Updating the Menu Data**:
   Expand your menu using a list of dictionaries:

   ```python
   def menu(request):
       new_menu = [
           {'name': 'Greek Salad', 'price': 7},
           {'name': 'Pasta', 'price': 10},
           {'name': 'Pizza', 'price': 12},
       ]
       return render(request, 'menu.html', {'menu': new_menu})
   ```

9. **Looping Through the Menu Items**:
   Update `menu.html` to display each item:

   ```html
   <h1>Menu</h1>
   <ul>
       {% for item in menu %}
           <li>{{ item.name }} - ${{ item.price }}</li>
       {% endfor %}
   </ul>
   ```

10. **Adding HTML for Styling**:
    Modify `menu.html` to display items in a table:

    ```html
    <h1>Menu</h1>
    <table>
        <tr>
            <th>Item</th>
            <th>Price</th>
        </tr>
        {% for item in menu %}
            <tr>
                <td>{{ item.name }}</td>
                <td>${{ item.price }}</td>
            </tr>
        {% endfor %}
    </table>
    ```

11. **Testing Dynamic Updates**:
    Add new items through the Django admin interface and refresh to see updates.

## Creating a Dynamic Menu in Django

1. **Understanding the Model**:
   Define a `Menu` model in `models.py`:

   ```python
   from django.db import models

   class Menu(models.Model):
       name = models.CharField(max_length=100)
       price = models.IntegerField()

       def __str__(self):
           return self.name
   ```

2. **Accessing Data in Django Admin**:
   Verify that your model contains data via the Django admin interface.

3. **Creating the View Function**:
   In `views.py`, create `menu_by_id`:

   ```python
   from django.shortcuts import render
   from .models import Menu

   def menu_by_id(request):
       new_menu = Menu.objects.all()
       return render(request, 'menu_card.html', {'menu': new_menu})
   ```

4. **Updating the URLs**:
   Map the path for the new view in `urls.py`:

   ```python
   urlpatterns = [
       path('menu_card/', views.menu_by_id, name='menu_card'),
   ]
   ```

5. **Creating the Template**:
   Create `menu_card.html` in the templates folder.

6. **Writing the Template Code**:

   ```html
   <h1>Menu</h1>
   {% if menu %}
       {% for item in menu %}
           <p>{{ item.name }} - ${{ item.price }}</p>
       {% endfor %}
   {% else %}
       <p>No menu items available.</p>
   {% endif %}
   ```

7. **Testing Your Code**:
   Run the server and visit `http://localhost:8000/menu_card/`.

8. **Adding Conditional Logic**:
   Ensure only items with values are displayed using the existing `if` statement.

9. **Formatting the Output**:
   Enhance the display of the menu items with HTML formatting.

10. **Dynamic Updates**:
    Add new items via the admin interface and refresh the page to see changes.

## Understanding Template Inheritance in Django

Template inheritance allows developers to create a consistent user interface across multiple pages without redundant code. Shared components like headers and footers can be managed efficiently.

### Key Concepts

1. **The DRY Principle**: Emphasizes that every distinct concept should exist in one place to avoid redundancy and maintenance issues.

2. **Using Base Templates**:
   Create a base template with common elements and define blocks for variable content that child templates can override.

3. **Understanding Blocks**:
   Use blocks to define sections of templates that child templates can fill in, such as headers and footers.

4. **The Include Tag**:
   Render a sub-template within a parent template, useful for reusable components.

### Example

**Base Template (`base.html`)**:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>{% block title %}Little Lemon{% endblock %}</title>
</head>
<body>
    {% include 'header.html' %}
    {% block content %}{% endblock %}
    {% include 'footer.html' %}
</body>
</html>
```

**Child Template (`about.html`)**:

```html
{% extends 'base.html' %}

{% block title %}About Us

{% endblock %}

{% block content %}
<h2>About Little Lemon</h2>
<p>We serve the best Mediterranean cuisine.</p>
{% endblock %}
```

## Template Inheritance and Static Files in Django

Using template inheritance with static files promotes a well-organized development process.

1. **Static Files Directory**:
   Place all CSS and JS files in a static directory (`/static/`).

2. **Settings Configuration**:
   Make sure you have `STATIC_URL` set in your `settings.py`:

   ```python
   STATIC_URL = '/static/'
   ```

3. **Loading Static Files**:
   Use the `{% load static %}` template tag to load static files:

   ```html
   {% load static %}
   <link rel="stylesheet" href="{% static 'css/styles.css' %}">
   ```

## Template Inheritance: Using Extends and Include Tags

1. **Create Views**:
   Define views for different pages (e.g., home, about).

2. **Update URL Configuration**:
   Ensure each view has a corresponding URL in `urls.py`.

3. **Settings Configuration**:
   Confirm your app and template directories are configured in `settings.py`.

4. **Folder Structure**:
   Organize your templates and static files effectively.

5. **Base Template Setup**:
   Create a `base.html` with common elements.

6. **Child Templates**:
   Create child templates using the `{% extends %}` tag and define their unique content in blocks.

7. **Incorporate Header**:
   Use the `{% include %}` tag for shared header content.

8. **Testing Your Setup**:
   Verify that all pages render correctly and display the expected dynamic content.
