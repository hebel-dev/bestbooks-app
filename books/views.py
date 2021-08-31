#from typing_extensions import Required
from .models import Author, AuthorComment, Book, BookComment
from books import forms

from django import template
from django.core.checks import messages
from django.core.validators import MaxLengthValidator

from django.forms.widgets import Widget
from books.forms import AuthorContactForm, LoginForm, RegisterForm

from django.http.response import HttpResponseRedirect
from django.http import HttpResponse, request

from django.urls.base import reverse_lazy
from django.urls import reverse

from django.utils import timezone

from django.views.generic.base import TemplateView
from django.views import generic
from django.views.generic.edit import FormView


from django.shortcuts import redirect, render
from django.template import context, loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login

# # version without html
# def index(request):
#     three_author_list = Author.objects.order_by('-surname_author')[:3]
#     txt = ''
#     for author in three_author_list:
#         txt += author.surname_author +' '+ author.name_author +'<br>'
#     return HttpResponse(f'{txt}')


# NEW VERSION 

# def index(request):
#     three_author_list = Author.objects.order_by('-surname_author')[:3]
#     # template = loader.get_template('books/index.html')
#     context = {
#         'three_author_list': three_author_list,
#         }
#     return render(request,'books/index.html',context)

class HomePage(generic.TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()[:3]
        print(context)
        return context
### OLD FUNCTION VERSION
# def authors_without_books(request):
#     authors = Author.objects.all()
#     template = loader.get_template('books/authors_list.html')
#     context = {
#         'authors':authors
#     }
#     return HttpResponse(template.render(context,request))
 
### NEW CLASS VERSION 
class AuthorListView(generic.ListView):
    model = Author
    template_name = 'books/authors_list.html'

# def author_with_all_books(request, author_id):
#     author = Author.objects.get(id=author_id)
#     all_books = author.book_set.all()
#     template = loader.get_template('books/author_with_books.html')
#     context = {
#         'author' : author,
#         'all_books' : all_books 
#     }
#     return HttpResponse(template.render(context,request))

class AuthorBooksView(generic.TemplateView):
    template_name = 'books/author_with_books.html'
    pk_url_kwarg = 'author_id'

    def get_context_data(self,author_id, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Author.objects.get(pk=author_id)
        context['all_books'] = context['author'].book_set.all()
        print(context)
        return context

# ### single book view
# def view_of_book(request, book_id):
#     book = Book.objects.get(id=book_id)
#     template = loader.get_template('books/book_of_author.html')
#     context = {
#         'book' : book,
#         # 'coments' : coments
#     }
#     return HttpResponse(template.render(context,request))

class BookView(generic.TemplateView):
    template_name = 'books/book_of_author.html'

    def get_context_data(self,book_id, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(id=book_id)
        print(context)
        return context

# def three_last_books(request):
#     all_books = Book.objects.order_by('-title_book')[:3]
#     template = loader.get_template('books/three_last_books.html')
#     context = {
#         'all_books' : all_books,
#     }
#     return render(request,'books/three_last_books.html', context)

class ThreeLastBooksView(generic.ListView):
    model = Book
    template_name = 'books/three_last_books.html'
class AuthorContactView(LoginRequiredMixin, FormView):
    form_class = AuthorContactForm
    template_name = 'books/contact.html'
    success_url =reverse_lazy('mail-send') 

    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        print('KWARGS',kwargs)
        print('ctx', ctx)  
        ctx['author'] = Author.objects.get(pk=self.kwargs.get('author_id'))
        
        return (ctx)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        #print('KWARGI',  kwargs)
        kwargs['author_id'] = self.kwargs.get('author_id')
        #print(kwargs['author_id'])
        return kwargs
    
    def form_valid(self, form):
        form.send_email()
        #print(form.cleaned_data)
        return super().form_valid(form)
    
class MailSendView(TemplateView):
    template_name = 'books/succes.html'

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'books/login.html'
    success_url = '/books/'

    def form_valid(self, form):
        user = authenticate(
            self.request, 
            username = form.cleaned_data['username'], 
            password = form.cleaned_data['password'],
            )
        if user is not None:
            login(self.request, user)
            if self.request.GET.get('next'):
                return HttpResponseRedirect(self.request.GET.get('next'))
            return HttpResponseRedirect('/books/')
        else:
            return HttpResponseRedirect(f"{reverse('login')}?next={self.request.GET.get('next')}")
        #return super(LoginView, self).form_valid(form)

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'books/register.html'
    success_url = '/books/'


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
    elif request.method == 'POST':
        print('WHere')
        print(request.POST)
        AuthorComment.objects.create(
            author_related= author,
            author = request.POST.get('author_who'),
            content = request.POST.get('content_what')
        )
        return HttpResponseRedirect(reverse('author_with_all_books', kwargs={'author_id' : author_id}))