from django.contrib import admin
from .models import Author, Book, BookComment

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookComment)

# Register your models here.
