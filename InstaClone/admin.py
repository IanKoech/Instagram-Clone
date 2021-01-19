from django.contrib import admin
from .models import Profile,Photo, Comments
# Register your models here.

admin.site.register(Photo)
admin.site.register(Profile)
admin.site.register(Comments)