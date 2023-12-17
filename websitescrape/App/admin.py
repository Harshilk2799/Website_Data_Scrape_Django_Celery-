from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "product_description"]