from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Image, Comments, Profile, Followers
import datetime as dt

#Creating views
def home(request):
    rendern render(request, 'home.html')

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
