from django import forms

class EmailPostForm(forms.Form):
    username = forms.CharField(max_length=25, label="Your name")
    sender_email = forms.EmailField()
    email_receiver = forms.EmailField()
    email_content = forms.CharField(required=False, widget=forms.Textarea)

