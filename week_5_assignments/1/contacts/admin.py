from django.contrib import admin

# Register your models here.

from .models import Contact, Category

admin.site.register(Contact)
admin.site.register(Category)
