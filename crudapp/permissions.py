from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'author'


class IsBookAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author
