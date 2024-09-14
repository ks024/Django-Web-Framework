## Django Web Framework Course Summary

- **Introduction:**
  - Django is an open-source Python framework for building large-scale web applications.
  - Requires knowledge of databases, Python, HTML, and CSS.

- **Course Structure:**
  - **Module 1:** Introduction to Django, including projects and apps, and the MVT pattern.
  - **Module 2:** Exploring views, handling HTTP requests/responses, URL patterns, and class-based views.
  - **Module 3:** Working with models, using Django admin, QuerySet API, forms, and MySQL database.
  - **Module 4:** Templates, template language, third-party libraries, debugging, and testing.
  - **Module 5:** Course recap and final project to create a data-driven web application for Little Lemon Restaurant.

- **Learning Approach:**
  - Watch and re-watch videos, engage with course readings, and complete exercises.
  - Participate in quizzes and discussions to reinforce learning.
  - Regular study schedule recommended for best results.

## Overview of Django Framework

- **What is Django?**
  - Open-source web development framework written in Python.
  - Initially created for a newspaper publisher's web application.
  - Ideal for high-text-content, media-rich, and high-traffic projects.

- **Benefits of Using Django:**
  - Provides essential components (templates, libraries, APIs) to avoid reinventing common features.
  - Ensures robust, secure, adaptable, and scalable functionalities.
  - Supports integration with various tools and other Python libraries.

- **Real-World Applications:**
  - **Publishing:** Handles large volumes of text and media.
  - **eCommerce, Healthcare, Finance:** Reliable for handling complex and secure transactions.
  - **Social Media & Networking:** Used by major platforms like Instagram for scalability.
  - **Machine Learning & AI:** Facilitates deployment of ML models via APIs, RPCs, and WebSockets.
  - **SaaS Applications:** Enhances performance with asynchronous views for concurrent processing.
  - **OTT Media Platforms:** Powers streaming services with high demand for scalability.

- **Key Features:**
  - **Scalability:** Easily adapts to growing user bases and resource demands.
  - **Fault Tolerance:** Reliable for large projects with high traffic.
  - **Cost-Effective:** Open-source nature reduces costs.
  - **Community & Documentation:** Strong support and comprehensive resources available.

- **Overall Advantages:**
  - Avoids redundant development.
  - Facilitates integration with various front-end frameworks.
  - Ideal for organizations needing a robust back-end framework.

**Additional Resources.**
- [Django official website](https://www.djangoproject.com/start/overview/)
- [Django documentation](https://docs.djangoproject.com/en/4.1/)
- [Installing VS Code on Mac - Official](https://code.visualstudio.com/docs/setup/mac)
- [Installing VS Code on Windows - Official](https://code.visualstudio.com/docs/setup/mac)
- [Django installation - Official](https://docs.djangoproject.com/en/4.1/topics/install/)
- [Install Django on Windows](https://docs.djangoproject.com/en/4.1/howto/windows/)
- [Setting up Virtual environment in Python - venv (Windows and MacOS)](https://docs.python.org/3/library/venv.html)

## Projects & Apps Overview
### Django Project and App Structure Overview

- **Website Basics:**
  - Static websites use HTML, CSS, and JavaScript.
  - Static sites may have simple folder structures (CSS, JavaScript, images).

- **Dynamic Web Applications:**
  - Require complex functionality (state management, data storage).
  - Frameworks like Django streamline development by avoiding repetitive tasks.

- **Django Framework Structure:**
  - **Project:**
    - Represents the entire web application.
    - Contains configuration and settings.
    - Django auto-generates this structure, organizing Python files and folders.
    - Simplifies development by focusing on code rather than configuration.

  - **App:**
    - A sub-module of a Django project.
    - Implements specific functionalities (e.g., news feed, user profiles).
    - Can be self-contained and reused across projects.
    - Created using the `startapp` command, generating a self-contained directory.
    - Must be added to `INSTALLED_APPS` in the project’s settings.

- **Core Concepts:**
  - **HTTP:** Essential for web communication; every action is tied to HTTP requests and URLs.
  - **Web Server:** Handles requests and responses; Django includes a development server.
  - **Database:** Stores and retrieves data; necessary for dynamic websites.
  - **Apps in Django:** Include models, views, templates, URLs, and more.

- **DRY Principle:**
  - “Don’t Repeat Yourself” – Write code once and reuse it across apps.

- **App Design:**
  - Apps should be feature-targeted and focused on a single purpose.
  - Project in Django can contain multiple apps, each responsible for a specific feature.

- **Application Registry:**
  - Maintains metadata for each installed app for configuration and introspection.

### Key Takeaways
- **Projects** are the overarching structure.
- **Apps** are modular, reusable components within a project.
- Understanding the difference and how to structure them is crucial for effective Django development.

## Project Structure
Use the `startproject` command of Django-admin as follows:
```bash
django-admin startproject demoproject 
```

```arduino
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        wsgi.py
        asgi.py
    app1/
        __init__.py
        admin.py
        apps.py
        models.py
        views.py
        urls.py
        migrations/
            __init__.py
        templates/
            app1/
                some_template.html
        static/
            app1/
                some_static_file.css
    app2/
        __init__.py
        admin.py
        apps.py
        models.py
        views.py
        urls.py
        migrations/
            __init__.py
        templates/
            app2/
                another_template.html
        static/
            app2/
                another_static_file.js
```

## Creating a Django App

To create a new app in a Django project, use:

```bash
python manage.py startapp <name_of_app>
```

This generates a directory with:

```
<name_of_app>/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
    migrations/
        __init__.py
    templates/  # Optional
    static/     # Optional
```

### Next Steps

1. Add the app to `INSTALLED_APPS` in `settings.py`:

   ```python
   INSTALLED_APPS = [
       '<name_of_app>',
   ]
   ```

## Django Management Commands

### `makemigrations`
Generates migration files for any changes made to your models. Run this command whenever you declare or modify models:

```bash
python manage.py makemigrations
```

### `migrate`
Applies migrations to synchronize the database with the current state of models and migrations:

```bash
python manage.py migrate
```

### `runserver`
Starts Django’s built-in development server on `127.0.0.1:8000`:

```bash
python manage.py runserver
```
