from django import forms
from django.forms import ModelForm
from .models import Post
from django.core.exceptions import ValidationError

class CreateForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a post...'
        }
    ))

    class Meta:
        model = Post
        fields = ('title','text')