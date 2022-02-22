from attr import fields
from django import forms
from django.forms import ModelForm
from .models import *


class IzvodacForm(ModelForm):
    class Meta:
        model = Izvodac
        fields = '__all__'

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ('naziv_albuma', 'godina_izdavanja_albuma', 'dodatne_informacije_albuma', 'izvodac')       

class PjesmaForm(ModelForm):
    class Meta:
        model = Pjesma
        fields = '__all__'