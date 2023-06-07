# Generated by Django 4.1.5 on 2023-03-13 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_rename_appointmentdate_bookdata_adate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookdata2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('visit', models.CharField(max_length=50)),
                ('adate', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Bookdata',
        ),
    ]
