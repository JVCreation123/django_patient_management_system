# Generated by Django 4.1.5 on 2023-03-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_patientdata_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdata',
            name='Gender',
            field=models.IntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'not selected')]),
        ),
    ]
