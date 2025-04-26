from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Note(models.Model):
    user = models.ForeignKey(to=User ,related_name='notes',on_delete=models.CASCADE)
    titel = models.CharField(max_length=100)
    text = models.TextField()
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    notes = models.ManyToManyField(to='Note',related_name='tags',null=True)