from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE
from django.db.models.fields import related
from django.utils import timezone

class Author (models.Model):
    name_author = models.CharField(max_length=20)
    surname_author = models.CharField(max_length=40)
    year_of_birth_autor = models.IntegerField(validators=[MaxValueValidator(2100), MinValueValidator(-2100)])

    def __str__(self):
        return f" Autor\ka {self.name_author} {self.surname_author}, rok urodzenia: {self.year_of_birth_autor}"

class Book (models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title_book = models.CharField(max_length=100)
    year_of_publishment = models.IntegerField(validators=[MaxValueValidator(2100), MinValueValidator(-2100)])

    def __str__(self):
        return self.title_book

### class Coment method by form
# class Coment(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     published_date = models.DateTimeField(blank=True, null=True)

#     def ___str__(self):
#         return self.text
    
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
    
class BookComment(models.Model):
    author = models.CharField(max_length=128)
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
