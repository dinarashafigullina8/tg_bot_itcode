# Generated by Django 4.1.7 on 2023-03-13 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_rename_application_requests'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Requests',
            new_name='Request',
        ),
    ]
