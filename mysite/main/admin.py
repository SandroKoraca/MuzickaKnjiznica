from django.contrib import admin
from .models import *

# Register your models here.

model_list = [Izvodac,Album,Pjesma]
admin.site.register(model_list)