from django import forms
from .models import Comment, Article
from django.contrib.auth.models import User


#####################  form for creating article   ######################

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['subject', 'message','college', 'picture']

#####################  form for creating comment   ######################

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Comments goes here','rows':'4', 'cols':'50'}))
    class Meta:
        model = Comment
        fields = ('content',)
