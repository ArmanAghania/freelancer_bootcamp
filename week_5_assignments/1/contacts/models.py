from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Contact(models.Model):
    first_name = models.CharField(max_length=122)
    last_name = models.CharField(max_length=122)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=12, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=122)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
