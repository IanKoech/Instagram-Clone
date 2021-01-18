from django import forms
from .models import Image, Comments, Profile

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'likes', 'captions']

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude =  ['user']

class Comment(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user', 'photo']
