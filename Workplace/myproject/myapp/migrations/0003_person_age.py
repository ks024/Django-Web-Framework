# Generated by Django 5.1.1 on 2024-09-23 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_name_person_person_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
