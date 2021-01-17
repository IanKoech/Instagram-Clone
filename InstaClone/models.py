from django.db import models

# Create your models here.

class Profile(models.Model):
    '''
    Class created columns in the Profile table
    Uses foreign key to link to Image class'''
    profile_photo = models.ImageField(upload_to = 'photos/')
    bio = models.TextField(max_length = 100)
    name = models.CharField(max_length = 30)

class Image(models.Model):
    '''
    Class creates columns in the image table
    '''
    name = models.CharField(max_length = 30)
    caption = models.CharField(max_length = 30)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
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
    def update_caption(self, newCaption):
        self.caption = this.newCaption
        self.save()





    