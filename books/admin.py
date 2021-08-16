from django.contrib import admin
from .models import Author, AuthorComment, Book, BookComment

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookComment)
admin.site.register(AuthorComment)

# Register your models here.
