from django.contrib import admin
from .models import alumni,experience,projects,Seminar

# Register your models here.

admin.site.register((alumni,experience,projects,Seminar))