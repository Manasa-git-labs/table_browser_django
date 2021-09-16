# Generated by Django 3.2.7 on 2021-09-15 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210915_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='name_basics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nconst', models.CharField(max_length=10)),
                ('primaryName', models.CharField(max_length=50)),
                ('birthYear', models.DateField()),
                ('deathYear', models.DateField()),
                ('primaryProfession', models.CharField(max_length=100)),
                ('knownForTitles', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='title_basics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tconst', models.CharField(max_length=10)),
                ('titleType', models.CharField(max_length=10)),
                ('primaryTitle', models.CharField(max_length=50)),
                ('originalTitle', models.CharField(max_length=50)),
                ('isAdult', models.CharField(max_length=2)),
                ('startYear', models.DateField()),
                ('endYear', models.DateField()),
                ('runtimeMinutes', models.CharField(max_length=10)),
                ('genres', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='title_principals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tconst', models.CharField(max_length=10)),
                ('ordering', models.CharField(max_length=10)),
                ('nconst', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('characters', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='title_ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tconst', models.CharField(max_length=10)),
                ('averageRating', models.CharField(max_length=5)),
                ('numVotes', models.CharField(max_length=10)),
            ],
        ),
    ]