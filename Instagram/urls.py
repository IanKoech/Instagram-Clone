"""Instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
#from django.contrib.auth import views as auth_views
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'', include('InstaClone.urls')),
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    #url('accounts/register/',
     #   RegistrationView.as_view(success_url='/'),
      #  name='django_registration_register'),
    #url('login/', auth_views.LoginView(template_name= 'login.html', name='login')),
    url('logout/', LogoutView, {"next_page": '/'}),     
    url(r'tinymce', include('tinymce.urls')),
    

]