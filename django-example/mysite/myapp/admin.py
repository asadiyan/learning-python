from django.contrib import admin
# we use . in importing here because the admin.py and models.py are in same directory
from .models import Book


# Register your models here.
# here we add the models(class or table) to see them in admin page 
admin.site.register(Book)
