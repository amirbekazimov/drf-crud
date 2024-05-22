from django.urls import path

from .views import BookList, BookDetail, AuthorList, AuthorDetail, GetAuthorBooks

urlpatterns = [
    # book urls
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('my-books/', GetAuthorBooks.as_view(), name='author-books'),
    # path('my-books/<int:pk>/', BookDetail.as_view(), name='book-detail'),

    # author urls
    path('author/', AuthorList.as_view(), name='author-list'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='author-detail')
]
