# Generated by Django 4.1.5 on 2023-03-13 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_delete_patient_remove_patientdata_gender2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=50)),
                ('Dob', models.DateField()),
                ('Reason', models.CharField(max_length=50)),
                ('Appointmentdate', models.DateField()),
            ],
        ),
    ]
