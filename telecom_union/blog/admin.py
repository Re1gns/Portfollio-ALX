from django.contrib import admin
from .models import Post, Comment, UserProfile

# Register your models here.

class CustomPost(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at", "featured")

class CustomUser(admin.ModelAdmin):
    list_display = ("user", "is_member")


admin.site.register(Post, CustomPost)
admin.site.register(Comment)
admin.site.register(UserProfile, CustomUser)
