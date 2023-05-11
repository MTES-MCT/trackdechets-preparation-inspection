from django.contrib import admin

from .models import FeedbackResult


@admin.register(FeedbackResult)
class FeedbackResultAdmin(admin.ModelAdmin):
    list_display = ["created", "author"]
