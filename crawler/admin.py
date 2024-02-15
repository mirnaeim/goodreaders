from django.contrib import admin
from django.contrib.admin import register

from .models import Book
# Register your models here.


@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'title', 'author', )
    list_display_links = ('title',)
    list_filter = ('rating',)
    search_fields = ('title', 'author')
