from django.contrib import admin
from .models import Post, Comment, UserProfile, ContactMessage

# Register your models here.


class CustomPost(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at", "featured")

class CustomUser(admin.ModelAdmin):
    list_display = ("user", "is_member")

class CustomContactMessage(admin.ModelAdmin):
    list_display = ("name", "subject", "date", "message")


admin.site.register(Post, CustomPost)
admin.site.register(Comment)
admin.site.register(UserProfile, CustomUser)
admin.site.register(ContactMessage, CustomContactMessage)
