from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    '''
    Class created columns in the Profile table
    Uses foreign key to link to Image class'''
    profile_photo = models.ImageField(upload_to = 'photos/')
    bio = models.TextField(max_length = 100)
    name = models.CharField(max_length = 30)
    user = models.ForeignKey(User, on_delete = models.CASCADE )
    followers = models.PositiveIntegerField(default=0)
    following  = models.PositiveIntegerField(default = 0)
    followers = models.ManyToManyField('self', related_name='is_following',blank=True)
    following = models.ManyToManyField('self', related_name='following',blank=True)

    @classmethod
    def save_profile(self):
        self.save()

    @classmethod
    def update_profile(self, bio):
        self.bio = bio if bio else self.bio
        self.save()

    @classmethod
    def delete(self):
        self.delete()

class Image(models.Model):
    '''
    Class creates columns in the image table
    '''
    name = models.CharField(max_length = 30)
    caption = models.CharField(max_length = 30)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField(max_length = 100)
    likes = models.IntegerField()
    image_url = models.ImageField(upload_to = 'images/')

    @classmethod
    def save_image(self):
        self.save()

    @classmethod
    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(self, caption):
        self.caption = caption if caption else self.caption
        self.save()





    