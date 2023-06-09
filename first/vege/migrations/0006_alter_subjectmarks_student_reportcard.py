# Generated by Django 4.2.1 on 2023-05-12 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0005_subject_subjectmarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmarks',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentmarks', to='vege.student'),
        ),
        migrations.CreateModel(
            name='Reportcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_rank', models.IntegerField()),
                ('date_of_report_card_generation', models.DateField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentreportcard', to='vege.student')),
            ],
            options={
                'unique_together': {('student_rank', 'date_of_report_card_generation')},
            },
        ),
    ]
