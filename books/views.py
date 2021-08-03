import books
from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book

def index(request):
    three_author_list = Author.objects.order_by('-surname_author')[:3]
    txt = ''
    for author in three_author_list:
        txt += author.surname_author +' '+ author.name_author +'<br>'
    return HttpResponse(f'{txt}')

def authors_without_books(request):
    authors = Author.objects.all()
    txt = ''
    for author in authors:
        txt += author.surname_author + ' ' + author.name_author + '<br>'
    return HttpResponse(f'lista autorów: <br> {txt}')

def author_with_all_books(request, author_id):
    author = Author.objects.get(id=author_id)
    all_books = author.book_set.all()
    txt = ''
    for book in all_books :
        txt += book.title_book + ' '
    return HttpResponse(f'hej oto nasz twórca : {author} <br> a o to lista jego utworów : <br> {txt}' )

