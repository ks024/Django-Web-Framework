from django.db import models

# Create your models here.
class Person(models.Model):
    person_name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.person_name