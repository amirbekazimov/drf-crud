from rest_framework.serializers import ModelSerializer

from .models import Book, Author


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'name',
            'last_name'
        )


class BookSerializer(ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'price',
            'isBestSeller',
            'author',
        )
