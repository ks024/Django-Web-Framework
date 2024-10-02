# Django Models and Migrations Guide

## Learning Objectives

- **Create Django models**: Understand how to define models and their relationships.
- **Apply migrations**: Learn to manage database schema changes effectively.
- **Utilize QuerySet API**: Perform CRUD operations efficiently.
- **Manage forms**: Bind data to models using Django's Form API.
- **User management**: Handle users and permissions via the Django admin.
- **Setup MySQL database**: Connect Django to a MySQL database for data management.

---

## Key Concepts

### Models

- **Definition**: Models are Python classes that represent database tables. Each model inherits from `django.db.models.Model`.
- **Attributes**: Each class attribute corresponds to a database field, allowing automatic management of data types and constraints.

### Migrations

- **Purpose**: Migrations are Django's way of propagating changes made to models (adding fields, deleting models, etc.) into the database schema.
- **Advantages**:
  - Synchronization between the database schema and the model definitions.
  - Easy version control of the database structure.
  - Simplified database maintenance without writing raw SQL.

---

## CRUD Operations

### Create

- Instantiate a model and save it:

  ```python
  user = User(first_name='John', last_name='Doe')
  user.save()
  ```

- Use the `create()` method:

  ```python
  User.objects.create(first_name='John', last_name='Doe')
  ```

### Read

- Retrieve a single record with `get()` or multiple records with `filter()`:

  ```python
  user = User.objects.get(id=1)
  users = User.objects.filter(last_name='Doe')
  ```

### Update

- Modify an existing record:

  ```python
  user = User.objects.get(id=1)
  user.last_name = 'Smith'
  user.save()
  ```

### Delete

- Delete a record:

  ```python
  user = User.objects.get(id=1)
  user.delete()
  ```

---

## Django Model Relationships

### 1. One-to-One Relationship

Used when a single record in one model is linked to a single record in another.

```python
class College(models.Model):
    college_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Principal(models.Model):
    college = models.OneToOneField(College, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
```

### 2. One-to-Many Relationship

One record in one model can relate to multiple records in another.

```python
class Subject(models.Model):
    subject_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
```

### 3. Many-to-Many Relationship

Multiple records in one model can relate to multiple records in another.

```python
class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    qualification = models.CharField(max_length=50)

class Subject(models.Model):
    subject_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    teachers = models.ManyToManyField(Teacher)
```

---

## Creating Models

### Steps to Create a Model

1. **Set Up the Project**: Ensure the Django project and app are created.
2. **Define the Model** in `models.py`:

   ```python
   from django.db import models

   class Menu(models.Model):
       name = models.CharField(max_length=100)
       cuisine = models.CharField(max_length=100)
       price = models.DecimalField(max_digits=5, decimal_places=2)

       def __str__(self):
           return self.name
   ```

3. **Run Migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Add Entries**:

   ```python
   Menu.objects.create(name='Pasta', cuisine='Italian', price=10.99)
   ```

5. **Retrieve Entries**:

   ```python
   menu_items = Menu.objects.all()
   ```

6. **Update Entries**:

   ```python
   item = Menu.objects.get(pk=1)
   item.cuisine = 'Vegetarian Italian'
   item.save()
   ```

7. **Using Django Admin**:
   Register the model in `admin.py`:

   ```python
   from django.contrib import admin
   from .models import Menu

   admin.site.register(Menu)
   ```

---

## Understanding Migrations

### Migration Commands

- **makemigrations**: Creates migration files based on model changes.
- **migrate**: Applies migrations to the database.
- **sqlmigrate**: Displays the SQL that will be executed for a migration.
- **showmigrations**: Lists the migration status for each app.

### Example Workflow

1. **Create a New App**:

   ```bash
   python manage.py startapp myapp
   ```

2. **Define a Model**:

   ```python
   class Person(models.Model):
       name = models.CharField(max_length=20)
   ```

3. **Create Migrations**:

   ```bash
   python manage.py makemigrations
   ```

4. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Check Migration Status**:

   ```bash
   python manage.py showmigrations
   ```

6. **Revert Migrations**:

   ```bash
   python manage.py migrate myapp 0001
   ```

---

## Applying Migrations

### Steps to Apply Migrations

1. **Set Up Project**: Confirm your app is in `INSTALLED_APPS`.
2. **Create Model**: Define your model in `models.py`.
3. **Make Migrations**:

   ```bash
   python manage.py makemigrations
   ```

4. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

5. **View Generated SQL**:

   ```bash
   python manage.py sqlmigrate myapp 0001
   ```

---

## Object-Relational Mapping (ORM) in Django

### Overview

Django’s ORM allows developers to interact with the database using Python objects rather than raw SQL, facilitating easier data management.

### Key Features

1. **Models**: Represents database tables.
2. **QuerySets**: Allows complex queries through Python methods.
3. **Creating Objects**: Use `.create()` or instantiate and call `.save()`.
4. **Updating and Deleting**: Modify attributes and use `.save()` or `.delete()` methods.

---

## Conclusion

Django's model and migration system provides a powerful framework for managing database structures and interactions. By utilizing models, migrations, and the ORM, developers can efficiently build and maintain robust web applications.

---

### Additional Resources

- [Django Models Documentation](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django Migrations Documentation](https://docs.djangoproject.com/en/stable/topics/migrations/)
- [Django Admin Documentation](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)
