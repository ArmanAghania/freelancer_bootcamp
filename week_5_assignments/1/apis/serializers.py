from rest_framework import serializers
from contacts.models import Contact, Category


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'address',
                  'phone_number', 'date_added', 'date_modified', 'category', 'user']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'user']
