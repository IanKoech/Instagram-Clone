from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls  import url

urlpatterns = [
    url(r'^$',views.photos, name = 'photos'),
    url(r'^profile/(\d+)$', views.profile, name = 'profile'),
    url(r'^new/$', views.addImages, name = 'addImages'),
    url(r'^update/$', views.updateProfile, name = 'profileUpdate'),
    url(r'^comment/(\d+)$', views.new_comment, name = 'comment'),
    url(r'^like/(\d+)$', views.like, name = 'like'),
    url(r'search/$', views.search, name = 'search')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)