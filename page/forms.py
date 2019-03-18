from django import forms
from .models import Comment, Contact, Projects




class SearchForm(forms.Form):
    q = forms.CharField(max_length=64)


class CommentForm(forms.ModelForm):
    text = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control',
               'placeholder': 'Wpisz co chcesz', }
    ))
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Imię:', 'size': '15px'}))

    class Meta:
        model = Comment
        fields = ('name', 'text',)


class ContactForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Imię:'}))
    # phone = forms.IntegerField(label='', widget=forms.TextInput(
    #     attrs={'class': 'form-control',
    #            'placeholder': 'Telefon:', 'size': '15px'}))
    mail = forms.EmailField(label='', widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'E-mail:'}))
    mesagge = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'form-control',
               'placeholder': 'Wpisz co chcesz',
               "cols": 50, "rows": 22}
    ))
    class Meta:
        model = Contact
        fields = ('name', 'mail')



class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'