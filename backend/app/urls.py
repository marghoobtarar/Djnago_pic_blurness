from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from . views import Imagecheck

urlpatterns = [
    path('image/', Imagecheck.as_view(), name='nameee')
]
