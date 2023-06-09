# Generated by Django 4.0.6 on 2023-03-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_prescriptiondata23_delete_prescriptiondata2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patientdata1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Gender', models.CharField(max_length=10)),
                ('Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Prescriptiondata233',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Medicine', models.CharField(max_length=50)),
                ('Date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Patientdata',
        ),
        migrations.DeleteModel(
            name='Prescriptiondata23',
        ),
    ]
