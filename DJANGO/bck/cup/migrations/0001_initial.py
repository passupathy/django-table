# Generated by Django 4.2.4 on 2024-01-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(default='', max_length=20)),
                ('AGE', models.CharField(default='', max_length=20)),
                ('MAIL', models.CharField(default='', max_length=20)),
                ('ADDRESS', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
