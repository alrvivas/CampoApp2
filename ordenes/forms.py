# encoding:utf-8
from django import forms
from .models import *


class ordenForm(forms.ModelForm):
    class Meta:
        model = Orden


class ordenproductoForm(forms.ModelForm):
    class Meta:
        model = OrdenProducto
