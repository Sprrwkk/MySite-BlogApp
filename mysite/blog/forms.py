from django import forms
from .models import Post, Comments
from django.forms import ModelForm

class EmailPostForm(forms.Form):
    username = forms.CharField(max_length=25)
    sender_email = forms.EmailField()
    email_receiver = forms.EmailField()
    email_content = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'body')

