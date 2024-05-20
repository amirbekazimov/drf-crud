from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BookList(APIView):

    @swagger_auto_schema(
        responses={200: openapi.Response('BookSerializer')},
    )
    def get(self, request):
        queryset = Book.objects.select_related('author').all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=BookSerializer,
        responses={201: openapi.Response('BookSerializer')},
        operation_id='CreateBook',
        operation_description='Create a new book',
        security=[],
        examples={
            'application/json': {
                'title': 'Example Book',
                'price': '10.00',
                'isBestSeller': 'false',
                'author': 'John Doe',
            }
        }
    )
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):

    @swagger_auto_schema(
        responses={200: openapi.Response('BookSerializer')},
    )
    def get(self, request, pk):
        queryset = Book.objects.get(pk=pk)
        serializer = BookSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=BookSerializer,
        responses={200: openapi.Response('BookSerializer')},
        operation_id='UpdateBook',
        operation_description='Update a book',
        security=[],
        examples={
            'application/json': {
                'title': 'Example Book',
                'price': '10.00',
                'isBestSeller': 'false',
                'author': 'John Doe',
            }
        },
    )
    def put(self, request, pk):
        queryset = Book.objects.get(pk=pk)
        serializer = BookSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={204: 'No Content'},
    )
    def delete(self, request, pk):
        queryset = Book.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# author views
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication, SessionAuthentication])
class AuthorList(APIView):
    swagger_auto_schema(
        request=AuthorSerializer,
        responses={200: openapi.Response('AuthorSerializer')},
    )

    @swagger_auto_schema(
        responses={200: openapi.Response('AuthorSerializer')},
    )
    def get(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=AuthorSerializer,
        responses={201: openapi.Response('AuthorSerializer')},
        operation_id='CreateAuthor',
        operation_description='Create a new author',
        security=[],
        examples={
            'application/json': {
                'name': 'John',
                'last_name': 'Doe',
            }
        }
    )
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(APIView):

    @swagger_auto_schema(
        responses={200: openapi.Response('AuthorSerializer')},
    )
    def get(self, request, pk):
        queryset = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=AuthorSerializer,
        responses={200: openapi.Response('AuthorSerializer')},
        operation_id='UpdateAuthor',
        operation_description='Update an author',
        security=[],
        examples={
            'application/json': {
                'name': 'John',
                'last_name': 'Doe',
            }
        },
    )
    def put(self, request, pk):
        queryset = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses={204: 'No Content'},
    )
    def delete(self, request, pk):
        queryset = Author.objects.get(pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
