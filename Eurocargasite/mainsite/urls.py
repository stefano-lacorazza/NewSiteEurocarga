from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("air_services/", views.air_services, name="air_services"),
    path("land_services/", views.land_services, name="land_services"),
    path("other_services/", views.other_services, name="other_services"),
    path("sea_services/", views.sea_services, name="sea_services"),
    path("team/", views.team, name="team"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
