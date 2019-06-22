from django import forms
from django.forms import ModelForm
from django.contrib import auth

from .models import Widget

class WidgetForm(forms.ModelForm):
    class Meta:
        model = Widget
        fields = ('desc', 'quant')


