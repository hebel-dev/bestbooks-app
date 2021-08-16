from django import template
from django.core.validators import MaxLengthValidator
from django.http.response import HttpResponseRedirect
from django.utils import timezone
import books
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Author, Book, BookComment
from django.template import context, loader
from django.urls import reverse


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
    # coments = book.coment_set.all()
    print(book)
    # print(coments)
    ####
    template = loader.get_template('books/book_of_author.html')
    context = {
        'book' : book,
        # 'coments' : coments
    }
    return HttpResponse(template.render(context,request))

### view of the last three books

def three_last_books(request):
    all_books = Book.objects.order_by('-title_book')[:3]
    template = loader.get_template('books/three_last_books.html')
    context = {
        'all_books' : all_books,
    }
    return render(request,'books/three_last_books.html', context)


### views to Comment in form.py version
# def new_coment(request,book_id):
    
#     #else:
#         form = ComentForm()
#         book = Book.objects.get(id=book_id)
        
#         context = {
#             'form' : form,
#             'book' : book
#         }
#         return render(request, 'books/new_coment.html', context)

# def author_coment(request, author_id):
#     author = Author.objects.get(id=author_id)

#     context = {
#         'author' : author,
#     }
#     return render(request, 'books/author_coment.html', context)
    

# def book_coment(request):
#     if request.method == "POST":
#         form = ComentForm(request.POST)
#         if form.is_valid():
#             coment = form.save(commit=False)
#             coment.published_date = timezone.now()
#             coment.save()
#             return redirect('books/book_of_author.html', pk=coment.pk)
#     else:        
#         form = ComentForm()
#     return render(request, 'books/book_of_author.html', {'form':form})

def create_book_coment_view(request, book_id):
    book = Book.objects.get(id = book_id)
    if request.method == 'GET':
        context = {
            'book' : book,
        }
        return render(request,'books/book_comment_form.html', context)
    elif request.method == 'POST':
        print('HHHUUURRRAAA')
        print(request.POST)      
        BookComment.objects.create(
            book = book,
            author = request.POST.get('author_kto_napisal'),
            content= request.POST.get('content_co_zostalo_napisane')

        )
        print
        return HttpResponseRedirect(reverse('view_of_book', kwargs={'book_id':book_id}))

def create_author_coment_view(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == 'GET':
        context = {
            'author' : author,
        }
        return render(request, 'books/author_comment_for.html', context)