# Generated by Django 4.2.1 on 2023-05-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_student_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='datetime1',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='number_of_bikes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
