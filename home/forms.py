from django import forms
from django.forms import ModelForm
from .models import Post
from django.core.exceptions import ValidationError

class CreateForm(forms.ModelForm):
    title= forms.CharField(required=True)
    

    class Meta:
        model = Post
        fields = ['title','text']

    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)

        # We only need to adjust picture if it is a freshly uploaded file
        # f = instance.   # Make a copy
        # if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
        #     bytearr = f.read()
        #     instance.content_type = f.content_type
        #     instance.picture = bytearr  # Overwrite with the actual image data

        if commit:
            instance.save()
            self.save_m2m() # Add this

        return instance