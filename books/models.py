from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Author (models.Model):
    name_author = models.CharField(max_length=20)
    surname_author = models.CharField(max_length=40)
    year_of_birth_autor = models.IntegerField(validators=[MaxValueValidator(2100), MinValueValidator(-2100)])



# Create your models here.
