from django.conf import urls
from django.urls import path

from . import views

urlpatterns = [

    path('', views.HomePage.as_view(), name='index'),
    path('autors/', views.AuthorListView.as_view(), name='authors_without_books'),
    path('<int:author_id>/books/', views.AuthorBooksView.as_view(), name='author_with_all_books'),
    path('<int:book_id>/book/', views.BookView.as_view(), name='view_of_book'),
    path('three_last/', views.HomePage.as_view(), name='three_last_authors'),
    path('three_last_books/', views.ThreeLastBooksView.as_view(), name='there_last_books'),
    path('book/<int:book_id>/add-comment/', views.create_book_coment_view, name='add-book-comment'),
    path('author/<int:author_id>/add-comment/',views.create_author_coment_view, name='add-author-comment'),
    path('contact/<int:author_id>/', views.AuthorContactView.as_view(), name='contact'),
    path('succes/', views.MailSendView.as_view(), name='mail-send' ),
    path('login/', views.LoginView.as_view(), name='login' ),
    path('register/', views.RegisterView.as_view(), name='register'),
    #path('contact/succes/', views.ContactFormView.as_view(), name='succes')  
    # path('<int:book_id>/new_coment/', views.new_coment, name='new_coment'),
    #path('<int:author_id>/author_coment', views.author_coment, name='author_coment'),

]

