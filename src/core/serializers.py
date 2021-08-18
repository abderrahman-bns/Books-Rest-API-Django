from django.db import models
from django.forms import fields
from rest_framework import serializers
from .models import Books


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = (
            'isbn',
            'title',
            'subtitle',
            'author',
            'published',
            'publisher',
            'pages',
            'description',
            'website',
        )