from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Image, Comments, Profile, Followers
import datetime as dt

#Creating views

def profile(request, id):
    try:
        user = User.objects.get(id = id)
        profile = Profile.objects.get(user = user)

    except:
        profile = None

    if profile == None:
        return redirect('profileupdate')
    else:
        return render(request, 'profile.html',{"user":user})

def photos(request):
    photos = Image.objects.all()
    profiles = Profile.objects.all()
    comments = Comments.objects.all()

    return render(request, 'profile.html',{"photos":photos, "profiles":profiles, "comments":comments})

def image(request):
    image = Image.objects.all()
    return render(request, 'image.html',{"photo":image})

def search(request):
    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        search_photos = Image.search(search_term)
        return render(request, 'search.html',{"results":search_photos})

    else:
        message  = 'The term you entered could not be found'

        return render(request, 'search.html',{"message":message})

def addImages(self):
    current_user =  request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
             image = form.save(commit = False)
             image.user = current_user
             image.likes = 0
             image.comments = 1

             image.save()
        return render(request, 'uploadImage.html',{"form":form, "image":image})
    
    else:
        form = NewImageForm()
        return render(request, 'uploadImage.html',{"form":form})

def updateProfile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProfile(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit  = False)
            profile.user = current_user
            profile.save()
        
        return redirect('profile')
    else:
        form = UpdateProfile()
        return render(request, 'updateProfile.html',{"form":form})

def new_comment(request, id):
    current_user = request.user
    image = Image.objects.get(id = id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.user = current_user
            comment.photo = photo

            comment.save()
        return redirect('photos')
    
    else:
        form = CommentForm()
        return render(request, 'comment.html',{"form":form, "photo":photo})

def like(request, id):
    image = Image.objects.get(id = id)
    image.likes = image.likes + 1
    image.save()

    return redirect('photos')