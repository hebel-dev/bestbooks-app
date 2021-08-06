from django import template
import books
from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book
from django.template import context, loader

# # version without html
# def index(request):
#     three_author_list = Author.objects.order_by('-surname_author')[:3]
#     txt = ''
#     for author in three_author_list:
#         txt += author.surname_author +' '+ author.name_author +'<br>'
#     return HttpResponse(f'{txt}')


# NEW VERSION 

def index(request):
    three_author_list = Author.objects.order_by('-surname_author')[:3]
    # template = loader.get_template('books/index.html')
    context = {
        'three_author_list': three_author_list,
        }
    return render(request,'books/index.html',context)

def three_last_authors():
    three_last_authors = Book.objects.order_by('title_book')[:3]
    context = {
        'three_last_authors': three_last_authors
    }

# version without html
# def authors_without_books(request):
#     authors = Author.objects.all()
#     txt = ''
#     for author in authors:
#         txt += author.surname_author + ' ' + author.name_author + '<br>'
#     return HttpResponse(f'lista autorów: <br> {txt}')


# NEW VERSION

def authors_without_books(request):
    authors = Author.objects.all()
    template = loader.get_template('books/authors_list.html')
    context = {
        'authors':authors
    }
    return HttpResponse(template.render(context,request))
 
# version without html 
# def author_with_all_books(request, author_id):
#     author = Author.objects.get(id=author_id)
#     all_books = author.book_set.all()
#     txt = ''
#     for book in all_books :
#         txt += book.title_book + ' '
#     return HttpResponse(f'hej oto nasz twórca : {author} <br> a o to lista jego utworów : <br> {txt}' )

# NEW VERSION

def author_with_all_books(request, author_id):
    author = Author.objects.get(id=author_id)
    all_books = author.book_set.all()
    template = loader.get_template('books/author_with_books.html')
    context = {
        'author' : author,
        'all_books' : all_books 
    }
    return HttpResponse(template.render(context,request))


### single book view
def view_of_book(request, book_id):
    book = Book.objects.get(id=book_id)
    print(book)
    template = loader.get_template('books/book_of_author.html')
    context = {
        'book' : book,
    }
    return HttpResponse(template.render(context,request))

### view of the last three books

#def three_last_b