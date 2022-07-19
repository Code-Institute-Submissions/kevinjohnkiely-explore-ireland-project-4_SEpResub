from django.contrib import admin
from .models import Location
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Location)
class LocationAdmin(SummernoteModelAdmin):

    summernote_fields = ('body')