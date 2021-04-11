from django.contrib import admin

# Register your models here.

from .models import DjangoClasses
# It almost feels like Django should be able to automatically register classes it detects
# within its project and app directories.
admin.site.register(DjangoClasses)
# But no, this silly little line is necessary.
# Maybe I don't WANT Django grabbing every class I write willy-nilly? Maybe the idea here is that
# the admin file is a switch, "yes, Django, please do register this class now"
