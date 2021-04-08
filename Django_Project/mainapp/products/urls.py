from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views


# Anatomy of a URL route:
# ('pattern to watch for', method to call, "shortcut name")
urlpatterns = [
    path('admin_console', views.admin_console, name="admin_console"),
]
