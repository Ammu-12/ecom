# Generated by Django 4.2.4 on 2023-08-09 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_category_created_category_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated',
        ),
    ]
