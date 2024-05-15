from django.contrib import admin

from crudapp.models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'isBestSeller', 'created_at', 'updated_at']
    list_filter = ['isBestSeller', 'created_at', 'updated_at']
    search_fields = ['title']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','last_name']
    list_filter = ['name','last_name']

