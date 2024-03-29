# Generated by Django 3.2.7 on 2021-09-15 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('firstname', models.CharField(default='', max_length=100)),
                ('lastname', models.CharField(default='xyz', max_length=100)),
                ('email', models.EmailField(default='', max_length=150, unique=True)),
                ('password', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
