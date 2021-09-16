from typing import Callable
from django.db import models
from django.db.models.deletion import CASCADE

class Profile(models.Model):
    email = models.EmailField(max_length=150,unique=True,default='')
    password = models.CharField(max_length=100,default='')

class DBList(models.Model):
    srno = models.IntegerField(unique=True)
    DBname = models.CharField(max_length=100,default='')

class Data(models.Model):
    name = models.ForeignKey(DBList,on_delete=models.CASCADE)
    # please add the remaining field which are required here

class links(models.Model):
    movieid = models.CharField(max_length=5)
    imdbid = models.CharField(max_length=10)
    tmdbid = models.CharField(max_length=10)

class movies(models.Model):
    movieid = models.CharField(max_length=5)
    title = models.CharField(max_length=100)
    geners = models.CharField(max_length=100)

class ratings(models.Model):
    userid = models.CharField(max_length=5)
    titleid = models.CharField(max_length=5)
    rating = models.CharField(max_length=5)
    timestamp = models.CharField(max_length=15)

class tags(models.Model):
    userid = models.CharField(max_length=5)
    titleid = models.CharField(max_length=5)
    tag = models.CharField(max_length=100)
    timestamp = models.CharField(max_length=15)
