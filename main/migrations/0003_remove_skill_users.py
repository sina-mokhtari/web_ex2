# Generated by Django 5.0.6 on 2024-06-16 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='users',
        ),
    ]