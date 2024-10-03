# Notes on Django Templates and Dynamic Content

## Table of Contents

1. [Introduction to Django Templates](#introduction-to-django-templates)
2. [HTML Response](#html-response)
3. [Using Variables in Responses](#using-variables-in-responses)
4. [Introduction to Templates](#introduction-to-templates)
5. [Rendering a Template](#rendering-a-template)
6. [Using Context with Templates](#using-context-with-templates)
7. [Conditional Logic and Looping in Templates](#conditional-logic-and-looping-in-templates)
8. [Filters in Django Template Language](#filters-in-django-template-language)
9. [Conclusion](#conclusion)
10. [Creating and Using Templates in Django](#creating-and-using-templates-in-django)
11. [Key Concepts](#key-concepts)
12. [The Render Function](#the-render-function)
13. [Steps to Create a Template in Django](#steps-to-create-a-template-in-django)
14. [Example: Creating an About Page for Little Lemon](#example-creating-an-about-page-for-little-lemon)
15. [Adding Dynamic Content](#adding-dynamic-content)

---

## Introduction to Django Templates

- **Dynamic Content**: Data that changes based on context, user behavior, and preferences.
- **Static Content**: HTML that remains unchanged.
- **Templates**: HTML files with placeholders for dynamic data, marked by the Django Template Language (DTL).

## HTML Response

- **Django View Function**: Returns an `HttpResponse` with the content-type "text/html" by default, allowing strings with HTML tags to be rendered in the browser.

### Basic HTML Response Example

```python
from django.http import HttpResponse 

def index(request): 
    return HttpResponse("<h1>Hello, world.</h1>")
```

- This function displays "Hello, world." within `<h1>` tags if the app is properly configured.

## Using Variables in Responses

- **Dynamic Responses**: Incorporate variables using Python’s string formatting. For example, to greet a person by name:

```python
from django.http import HttpResponse 

def index(request, name): 
    return HttpResponse("<h1>Hello, {}.</h1>".format(name))
```

### Limitations of String Responses

- Generating HTML directly from Python can become complicated, especially when incorporating multiple variables or conditional logic.

## Introduction to Templates

- **Templates**: HTML files containing placeholders for dynamic content, using DTL for dynamic variable insertion.

### Example of a Simple Template

Create a `hello.html` file:

```html
<html> 
<head> 
    <title>My Django Website</title> 
</head> 
<body> 
    <h1>Hello World</h1> 
</body> 
</html>
```

## Rendering a Template

- Import the `loader` class from `django.template` and render the template as part of the HTTP response:

```python
from django.http import HttpResponse 
from django.template import loader 

def index(request): 
    template = loader.get_template('hello.html') 
    context = {} 
    return HttpResponse(template.render(context, request))
```

### Using the `render()` Shortcut

- Django offers a shortcut that simplifies the rendering process:

```python
from django.shortcuts import render 

def index(request): 
    return render(request, 'hello.html', {})
```

## Using Context with Templates

- **Template Context**: Pass context variables to the template. For example:

```python
from django.shortcuts import render 

def index(request, name):  
    context = {"name": name}  
    return render(request, 'hello.html', context)
```

- Update `hello.html` to include the variable:

```html
<html>  
<body>  
    <h1>Hello {{ name }}</h1>  
</body>  
</html>
```

## Conditional Logic and Looping in Templates

- DTL allows for conditional logic and loops within templates:
  - **Conditional Logic**: Use `{% if condition %} ... {% endif %}` for conditions.
  - **Looping**: Use `{% for item in list %} ... {% endfor %}` to iterate over items.

## Filters in Django Template Language

- **Filters**: Modify the output of template variables using the pipe (`|`) symbol. For example, applying the `upper` filter converts the variable to uppercase:

```html
{{ name | upper }}
```

### Common Filters

- **Upper and Lower**:
  - `{{ name | upper }}`: Converts the value to uppercase.
  - `{{ name | lower }}`: Converts the value to lowercase.

- **Title**:
  - `{{ string | title }}`: Capitalizes the first letter of each word.

- **Length**:
  - `{{ nums | length }}`: Returns the number of items in a list.

- **Wordcount**:
  - `{{ string | wordcount }}`: Counts the number of words in a string.

- **Slice**:
  - `{{ nums | slice:":3" }}`: Returns a portion of the list based on the provided indices.

- **First and Last**:
  - `{{ nums | first }}`: Returns the first item in a list.
  - `{{ nums | last }}`: Returns the last item in a list.

## Conclusion

Django templates provide a powerful way to generate dynamic HTML content, utilizing a clear syntax for variables, filters, and control structures. Understanding how to implement templates effectively is crucial for developing robust web applications in Django.

---

## Creating and Using Templates in Django

## Key Concepts

- **View Functions**: Retrieve data from databases or other data structures and prepare it for rendering in templates.
- **Django Template Language (DTL)**: Used to display dynamic data alongside static HTML.

### The Render Function

The `render` function is essential for displaying templates in Django and takes three parameters:

1. **request**: Represents the initial HTTP request object.
2. **path**: The relative path to the HTML file in the templates directory.
3. **dictionary**: Contains variables as keys that the template can use to display dynamic data.

### How the Render Function Works

- The `render` function returns a string as part of the HTTP response object, which the web page renders. This allows flexibility in defining and passing variables to templates.

## Steps to Create a Template in Django

1. **Define a View**: Create a view function that uses the `render` function.
2. **Update URL Configurations**: Modify the URL patterns in `urls.py` to link to the view.
3. **Configure Settings**: Ensure templates are configured in `settings.py` under the `DIRS` key and the app is registered in `INSTALLED_APPS`.
4. **Create an HTML Page**: Use DTL to create a file with static HTML and dynamic data.
5. **Pass Template and Context**: Use the `render` function to pass the template name and context dictionary.

## Example: Creating an About Page for Little Lemon

1. **Create a View Function**:
   - In `views.py`, create a view function called `about` that takes the `request` object and returns the `about.html` template.

   ```python
   from django.shortcuts import render

   def about(request):
       return render(request, 'about.html')
   ```

2. **Update URL Configuration**:
   - Ensure that the `urls.py` files (both project and app levels) are updated to include the `about` view.

3. **Configure Template Settings**:
   - In `settings.py`, add the templates directory under the `DIRS` key and confirm the app is registered.

4. **Create `about.html`**:
   - In the main project directory, create a `templates` folder and a file named `about.html` using the basic HTML structure.

   ```html
   <html>
   <head>
       <title>About - Little Lemon</title>
   </head>
   <body>
       <h2>About</h2>
   </body>
   </html>
   ```

5. **Run the Server**:
   - Start the server with `python3 manage.py runserver` and navigate to `localhost:8000/about` to view the template.

## Adding Dynamic Content

1. **Create a Dictionary in `views.py`**:
   - Add a dictionary called `about_content` with key-value pairs for additional content.

   ```python
   def about(request):
       about_content = {
           "about": "Little Lemon is a fantastic restaurant offering delicious dishes."
       }
       return render(request, 'about.html', about_content)
   ```

2. **Update `about.html`**:
   - Add a paragraph tag to display dynamic content using the template variable syntax.

   ```html
   <p>{{ about }}</p>
   ```

3. **Refresh the Page**:
   - After saving changes, refresh the browser to see the updated content.

4. **Add Styling**:
   - Enhance the appearance by adding CSS styling in the `<style>` section or linking to an external stylesheet.

This example demonstrates how to create an HTML template in Django, incorporating both static content (headings) and dynamic content (paragraphs). You have learned to use the Django template language effectively, setting the stage for more advanced template features in future projects.
