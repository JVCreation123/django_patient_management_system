# Generated by Django 4.0.6 on 2023-03-22 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_bookdata_delete_bookdata2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paymentdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Cvv', models.IntegerField(max_length=3)),
                ('Card', models.IntegerField(max_length=10)),
            ],
        ),
    ]
