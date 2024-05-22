from django.db import models
from authapp.models import CustomUser


class Book(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    isBestSeller = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} {self.last_name}'
