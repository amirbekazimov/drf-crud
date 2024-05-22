# Generated by Django 5.0.6 on 2024-05-21 23:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_remove_customuser_confirm_password_and_more'),
        ('crudapp', '0004_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authapp.customuser'),
        ),
    ]
