from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=200)
    roll_no=models.IntegerField(default=01,null=False,unique=True)
class test(models.Model):
    subject=models.CharField(max_length=200)
