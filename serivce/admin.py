from django.contrib import admin

# Register your models here.
from .models import Car, Instructor

admin.site.register(Car)
admin.site.register(Instructor)