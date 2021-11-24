from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('upload/', upload, name="upload"),
    path('profile/', profile, name="profile"),
    path('autosuggest/', autosuggest, name="autosuggest"),
    path('search/', search, name="search"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
