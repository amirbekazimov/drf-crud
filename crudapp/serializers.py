from rest_framework.serializers import ModelSerializer

from authapp.serializers import UserSerializer
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
    author = UserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'price',
            'isBestSeller',
            'author',
        )

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
