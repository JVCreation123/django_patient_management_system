# Generated by Django 4.1.5 on 2023-03-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_patientdata_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdata',
            name='Gender',
            field=models.IntegerField(max_length=50),
        ),
    ]
