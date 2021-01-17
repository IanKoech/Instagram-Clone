from django.shortcuts import render, redirect
from .models import Image, Profile
from django.http import request, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url= '/accounts/login/')
def profile(request, id):
    try:
        user = User.objects.get(id = id)
        profile = Profile.objects.get(user = user)
    except:
        profile = None
   
    if profile == None:
        return redirect('profileupdate')
    else:
        return render(request, 'profile.html', {"user":profile})

@login_required(login_url= '/accounts/login/')
def photos(request):

    Photos = Photo.objects.all()
    Profiles = Profile.objects.all()
    

    return render(request, 'photos.html', {"photos":Photos, "profiles":Profiles, "comments":comments})

@login_required(login_url= '/accounts/login/')
def image(request, id):

    image = Photo.objects.get(id =id)

    return render(request, 'image.html', {"photo": image})


@login_required(login_url= '/accounts/login/')
def search(request):

    if 'username' in request.GET and request.GET["username"]:
        searched_term = request.GET.get("username")
        searched_photos = Photo.search(searched_term)

        return render(request, 'search.html', {"results":searched_photos})

    else:
        message = 'The search term you entered is not available'

        return render(request, 'search.html', {"message":message})

@login_required(login_url= '/accounts/login/')
def addphotos(request):
    current_user = request.user 
    if request.method == 'POST':
        form = NewPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            
            photo = form.save(commit = False)
            photo.user = current_user
            photo.likes = 0
            photo.comments = 1

            photo.save()
        return render(request, 'post.html',{"form": form, "photo":photo})

    else:
        form = NewPhotoForm()

        return render(request, 'post.html',{"form": form})

@login_required(login_url= '/accounts/login/')
def profileupdate(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProfile(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            

        return redirect('profile')

    else:
        form = UpdateProfile()

        return render(request, 'updateprofile.html',{"form":form})

@login_required(login_url= '/accounts/login/')
def new_comment(request, id):
    current_user = request.user
    photo = Photo.objects.get(id =id)
    if request.method == 'POST':
        form = Comment(request.POST, request.FILES)
        if form.is_valid():
            
            comment = form.save(commit=False)
            comment.user = current_user
            comment.photo = photo
            

            comment.save()
        return redirect('photos')     

    else:
        form = Comment()       

        return render(request, 'comment.html', {"form":form, "photo":photo})

@login_required(login_url= '/accounts/login/')
def like(request, id):
    photo = Photo.objects.get(id = id)
    photo.likes = photo.likes + 1
    photo.save()

    return redirect('photos')    
