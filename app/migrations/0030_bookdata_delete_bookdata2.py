# Generated by Django 4.0.6 on 2023-03-22 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_patientdata2_delete_patientdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('visit', models.CharField(max_length=50)),
                ('adate', models.DateField()),
                ('atime', models.TimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Bookdata2',
        ),
    ]
