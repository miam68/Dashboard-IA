# Generated by Django 3.1.3 on 2021-06-09 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20210609_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='atachement',
        ),
        migrations.RemoveField(
            model_name='message',
            name='expediteur',
        ),
    ]
