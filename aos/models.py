from django.db import models
from django.contrib.auth.models import User
from django import forms
from google.appengine.ext import db

class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User)
    
class Session(models.Model):
    owner = models.EmailField()
    date = models.DateTimeField(auto_now_add = True)


class Person(db.Model):
    name = db.StringProperty(required=True)
    age = db.IntegerProperty(default=18)

    def is_old(self):
        return self.age >= 80
    
class Greeting(models.Model):
    author = models.ForeignKey(User, null=True, blank=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)