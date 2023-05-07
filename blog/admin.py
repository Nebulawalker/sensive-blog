from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdminSettings(admin.ModelAdmin):
    raw_id_fields = ['author', 'tags', 'likes']
    list_display = ['title']


@admin.register(Comment)
class CommentAdminSettings(admin.ModelAdmin):
    raw_id_fields = ['author', 'post']
    list_display = ['author', 'post']


@admin.register(Tag)
class TagAdminSettings(admin.ModelAdmin):
    list_display = ['title']
