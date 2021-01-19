from django.test import TestCase
from .models import Comments, Photo,Profile
from django.contrib.auth.models import User
# Create your tests here.

class testProfile(TestCase):
    def setUp(self):
        self.new_user = User(password='Stanford2020*',username='Sandys',is_superuser=False)
        self.new_user.save()
        self.new_profile = Profile(id =1000, name='Dan',bio='Dancan Sandys', user=self.new_user)

    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()

    def testinstance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def testprofilesaved(self):

        self.new_profile.saveprofile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def testdeleteprofile(self):

        self.new_profile.saveprofile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        self.new_profile.deleteprofile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) < 2)

class testPhoto(TestCase):
    def setUp(self):
        self.new_user = User(password='Stanford2020*',username='Sandys',is_superuser=False)
        self.new_user.save()
        self.new_photo = Photo(id = 1000,name='deans',user=self.new_user,captions='The greatest',likes=0)

    def tearDown(self):
        User.objects.all().delete()
        Photo.objects.all().delete()

    def testinstance(self):
        self.assertTrue(isinstance(self.new_photo,Photo))

    def testphotosaved(self):
        self.new_photo.savephoto()
        photos = Photo.objects.all()
        self.assertTrue(len(photos)> 0)

    def testdeletephoto(self):
        self.new_photo.savephoto()
        photos = Photo.objects.all()
        self.assertTrue(len(photos)> 0)
        self.new_photo.deletephoto()
        photos = Photo.objects.all()
        self.assertTrue(len(photos)<2)

class testComments(TestCase):
    def setUp(self):
        self.new_user = User(password='Stanford2020*',username='Sandys',is_superuser=False)
        self.new_user.save()
        self.new_photo = Photo(id = 1000,name='deans',user=self.new_user,captions='The greatest',likes=0)
        self.new_photo.savephoto()
        self.new_comment = Comments(id = 1000, user = self.new_user, photo= self.new_photo,comment='No')

    def tearDown(self):
        User.objects.all().delete()
        Photo.objects.all().delete()
        Comments.objects.all().delete()

    def testinstance(self):
        self.assertTrue(isinstance(self.new_comment, Comments))

    def testcommentsaved(self):
        self.new_comment.savecomments()
        comments = Comments.objects.all()
        self.assertTrue(len(comments)> 0)


    def testdeletecomment(self):
        self.new_comment.savecomments()
        comments = Comments.objects.all()
        self.assertTrue(len(comments)> 0)

        self.new_comment.deletecomments()
        self.new_user.delete()
        self.new_photo.deletephoto()
        comments = Comments.objects.all()
        self.assertTrue(len(comments) < 1)