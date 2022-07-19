from django.contrib import admin
from .models import Location, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Location)
class LocationAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_at', 'creator')
    search_fields = ['content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_at')
    summernote_fields = ('body')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'location', 'created_at', 'comment_approved')
    list_filter = ('comment_approved', 'created_at')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_location_comments']

    def approve_location_comments(self, request, queryset):
        queryset.update(comment_approved=True)

