# Generated by Django 4.0.6 on 2023-03-18 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_admin_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='admin_log',
            name='Password',
            field=models.CharField(max_length=10),
        ),
    ]