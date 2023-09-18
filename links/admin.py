from django.contrib import admin
from .models import Link # to acess the class Link model created in .models.py

# Register your models here.
admin.site.register(Link) # have to create a superuser to register and log in :), runserver to check
