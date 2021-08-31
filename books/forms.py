from django.db.models.query import QuerySet
from django.forms.fields import CharField
from books.models import Author
from django import forms
from django.core.mail import send_mail 


class AuthorContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    terms_of_use = forms.BooleanField(required=True)
    # author = forms.ModelChoiceField(queryset=Author.objects.all())

    def __init__(self,*args,**kwargs):
        print(kwargs)
        self.author_id = kwargs.pop('author_id')
        print(kwargs)
        super().__init__(*args, **kwargs)

    
    def send_email(self):
        name = self.cleaned_data.get('name'),
        message = self.cleaned_data.get('message'),
        author = Author.objects.get(pk=self.author_id)
        send_mail(
            subject = f'New comment to site {name}',
            message = f'message{message}',
            from_email = 'no-replay@mojastrona.wp.pl',
            recipient_list= [f'{author.name_author}_{author.surname_author}@bestbooks.pl']

        )

class LoginForm(forms.Form):
    username = forms.CharField(label='login')
    password = forms.CharField(label='password', widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label='login')
    password = forms.CharField(label='password')
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password_repeat = forms.CharField(label='repeat password', widget=forms.PasswordInput)
    