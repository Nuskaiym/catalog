from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_filter = ('user_name', 'phone', 'title', 'text')
    list_display = ('user_name', 'phone', 'title', 'text')