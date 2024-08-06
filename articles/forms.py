from django import forms
from .model import Article


class ArticleForm(forms.ModelForm):
    class meta():
        model = Article
        #fields = '__all__'
        exlude = ('user', )

