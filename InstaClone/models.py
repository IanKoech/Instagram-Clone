from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length = 60)
    bio = models.TextField(max_length =130)
    profile_photo = models.ImageField(upload_to = 'images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def saveprofile(self):
        self.save()

    def deleteprofile(self):
        self.delete()

    def updateprofile(self, bio):
        self.bio = bio if bio else self.bio
        self.save()

    
class Image(models.Model):

    photo_url = models.ImageField(upload_to= 'images/')
    name = models.CharField(max_length =100)
    user = models.ForeignKey(User, on_delete = models.CASCADE,)
    likes = models.IntegerField()
    captions = models.TextField(max_length =160)  
      
    def __str__(self):
        return self.name

    def savephoto(self):
        self.save()

    def deletephoto(self):
        self.delete()

    def updatephoto(self, photo):
        self.photo_url = photo if photo else self.photo_url
        self.save()

    def likephoto(self):
        self.likes = likes + 1
        self.save()

    @classmethod
    def search(cls, searched_term):
        user = User.objects.filter(username=searched_term)
        photos = Photo.objects.filter(user=user)
        return photos

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length = 500)
    photo = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    def savecomments(self):
        self.save()

    def deletecomments(self):
        self.delete()

    def updatecomments(self, comment):
        self.comment = comment if comment else self.comment
        self.save()

class Followers(models.Model):
    user = models.CharField(max_length=30)

    def __str__(self):
        return self.user