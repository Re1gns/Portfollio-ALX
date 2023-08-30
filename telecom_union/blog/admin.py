from django.contrib import admin
from .models import Post, Event, Comment, UserProfile, ContactMessage, JoinApplication

# Register your models here.


class CustomPost(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at", "featured")

class CustomEvent(admin.ModelAdmin):
    list_display = ("title", "slug", "event_date", "created_at")

class CustomUser(admin.ModelAdmin):
    list_display = ("user", "is_member")

class CustomMember(admin.ModelAdmin):
    list_display = ("user", "full_name", "age", "gender", "job_title", "employment_status", "timestamp")

class CustomContactMessage(admin.ModelAdmin):
    list_display = ("name", "subject", "date", "message")


admin.site.register(Post, CustomPost)
admin.site.register(Event, CustomEvent)
admin.site.register(Comment)
admin.site.register(JoinApplication, CustomMember)
admin.site.register(UserProfile, CustomUser)
admin.site.register(ContactMessage, CustomContactMessage)
