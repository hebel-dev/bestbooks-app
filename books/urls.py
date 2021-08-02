from django.conf import urls
from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('autors/', views.authors_without_books, name='authors_without_books'),
    path('<int:author_id>/books', views.author_with_all_books, name='author_with_all_books')

    

]

