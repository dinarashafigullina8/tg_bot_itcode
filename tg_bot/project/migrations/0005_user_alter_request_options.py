# Generated by Django 4.1.7 on 2023-03-15 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_rename_requests_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки'},
        ),
    ]
