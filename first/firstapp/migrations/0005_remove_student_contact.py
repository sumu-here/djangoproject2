# Generated by Django 4.2.1 on 2023-05-06 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_remove_student_datetime1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='contact',
        ),
    ]
