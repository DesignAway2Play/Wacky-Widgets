from django.db import models
from django.forms import ModelForm

# Create your models here.


class Widget(models.Model):
    desc  = models.CharField(max_length=100)
    quant = models.IntegerField(default=0)
