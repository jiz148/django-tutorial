# Generated by Django 3.1.3 on 2020-12-08 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auto',
            old_name='comment',
            new_name='comments',
        ),
    ]