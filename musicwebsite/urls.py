from django.conf.urls import url, include
from django.contrib import admin

from music import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/$',include('music.urls')),
    url(r'^music/(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^music/(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),


]
