# Generated by Django 4.0.6 on 2023-03-23 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_patientdata_prescriptiondata2_delete_patientdata2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescriptiondata23',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Medicine', models.CharField(max_length=50)),
                ('Date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Prescriptiondata2',
        ),
    ]
