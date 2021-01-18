from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls  import url

urlpatterns = [
    url(r'^$',views.photos, name = photos),
    url()
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)