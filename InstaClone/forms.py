from .models import Photo, Profile, Comments
from django import forms

class NewPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['user','comments', 'likes','date']

class UpdateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class Comment(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user', 'photo']