from django import forms
from django.forms import ModelForm
from .models import Post
# from django.core.exceptions import ValidationError


class CreateForm(forms.ModelForm):

    title = forms.CharField(required=True) # defining the field as not required

    # Meta class is there for defining and altering various metadata features
    class Meta:
        model = Post
        fields = ['title','text','date_posted']

    # def clean(self): # validation function
    #     cleaned_data = super(CreateForm, self).clean()

    #     input_field_1 = cleaned_data.get('title') # getting input from the title field
    #     input_field_2 = cleaned_data.get('text') # getting input from the content field

    #     if input_field_1 is not None and input_field_2 is not None:
    #         if len(input_field_2)<3:
    #             # self.add_error(None, ValidationError('The title should be different')) # non-field error
    #             self.add_error('text', ValidationError('The message is too short')) 


class UpdateForm(forms.ModelForm):

    title = forms.CharField(required=False)
    text = forms.CharField(required=False)
    # text_clear = forms.BooleanField(required=False)

    class Meta:
        model = Post
        fields = ['title','text','date_posted']

    # def clean(self):
    #     cleaned_data = super(UpdateForm, self).clean()

    #     input_field_1 = cleaned_data.get('title')
    #     input_field_2 = cleaned_data.get('text')
    #     input_field_3 = cleaned_data.get('updated_at')

    #     if input_field_1 is not None and input_field_2 is not None:
    #         if len(input_field_2)<3:
    #             self.add_error('text', ValidationError('The message is too short'))

# class CreateViewForm(forms.ModelForm):
#     title= forms.CharField(required=True)
    

#     class Meta:
#         model = Post
#         fields = ['id','title','text']

#     def save(self, commit=True):
#         instance = super(CreateViewForm, self).save(commit=False)

#         # We only need to adjust picture if it is a freshly uploaded file
#         # f = instance.   # Make a copy
#         # if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
#         #     bytearr = f.read()
#         #     instance.content_type = f.content_type
#         #     instance.picture = bytearr  # Overwrite with the actual image data

#         if commit:
#             instance.save()
#             self.save_m2m() # Add this

#         return instance