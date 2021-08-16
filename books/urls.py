from django.conf import urls
from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('autors/', views.authors_without_books, name='authors_without_books'),
    path('<int:author_id>/books/', views.author_with_all_books, name='author_with_all_books'),
    path('<int:book_id>/book/', views.view_of_book, name='view_of_book'),
    path('three_last/', views.index, name='three_last_authors'),
    path('three_last_books/', views.three_last_books, name='there_last_books'),
    path('<int:book_id>/new_coment/', views.new_coment, name='new_coment'),
    path('<int:author_id>/author_coment', views.author_coment, name='author_coment'),
]

