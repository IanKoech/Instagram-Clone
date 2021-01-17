from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
from django.core.exceptions import ObjectDoesNotExist

# import datetime as dt


class Profile(models.Model):
    photo = CloudinaryField("photo")
    name = models.CharField(max_length=15)
    userName = models.CharField(max_length=15, null=True)
    bio = models.CharField(max_length=50, null=True, blank=True)
    posts = models.PositiveIntegerField(null=True, blank=True)
    followers = models.PositiveIntegerField(default=0)
    following = models.PositiveIntegerField(default=0)
    followers = models.ManyToManyField('self', related_name='is_following',blank=True)
    following = models.ManyToManyField('self', related_name='following',blank=True)

    def __str__(self):
        return self.name

    def saveProfile(self):
        return self.save()

    def deleteProfile(self):
        return self.delete()

    @classmethod
    def getProfileById(cls, pk):
        try:
            prlObject = cls.objects.get(id=pk)
            return prlObject
        except ObjectDoesNotExist:
            message = "Profile does not exist"
            return message

    @classmethod
    def updateProfile(cls, pk, data):
        profileUpdate = cls.getImageById(pk)
        if profileUpdate:
            Profile.objects.filter(id=data[pk]).update(
                photo=data["photo"], name=data["name"], bio=data["bio"]
            )
            message = "Image was updated successfully"
            return message
        else:
            message = "Image does not exist"
            return message

class UserFollowing(models.Model):
    userId = models.ForeignKey(Profile, related_name="followingId", on_delete=models.CASCADE)
    followingUserId = models.ForeignKey(Profile, related_name="followersId", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['userId','followingUserId'],  name="unique_followers")
        ]

        ordering = ["-created"]

    def __str__(self):
        f"{self.userId} follows {self.followingUserId}"

class Comment(models.Model):
    comment = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pubDate = models.DateTimeField(auto_now=True)


class Image(models.Model):
    image = CloudinaryField("image", null=True)
    imageCaption = models.CharField(max_length=30)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="imageProfile"
    )
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="imageComment", null=True
    )
    # sender = models.ForeignKey(User,on_delete=models.CASCADE)
    noOfLikes = models.PositiveIntegerField(default=0)
    noOfComments = models.PositiveIntegerField(default=0)
    pubDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.imageCaption

    def saveImage(self):
        return self.save()

    def deleteImage(self):
        return self.delete()

    @classmethod
    def getImageById(cls, pk):
        try:
            imgObject = cls.objects.get(id=pk)
            return imgObject
        except ObjectDoesNotExist:
            message = "Image does not exist"
            return message

    @classmethod
    def updateImage(cls, pk, newImage):
        imageUpdate = cls.getImageById(pk)
        if imageUpdate:
            Image.objects.filter(id=pk).update(image=newImage)
            message = "Image was updated successfully"
            return message
        else:
            message = "Image does not exist"
            return message

    # list images from most recent method
    @classmethod
    def timeline(cls):
        timelineImages = cls.objects.latest("pub_date")
        return timelineImages