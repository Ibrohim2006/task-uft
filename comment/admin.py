from django.contrib import admin
from .models import Comment
from parler.admin import TranslatableAdmin
from django.utils.html import format_html
# Register your models here.

@admin.register(Comment)
class CommentAdmin(TranslatableAdmin):
    list_display = ('first_name', 'last_name', 'job', 'company', 'image_tag', 'feedback_file')
    search_fields = ('first_name', 'last_name', 'job', 'company')

    def image_tag(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; border-radius: 50%;" />', obj.profile_image.url)
        return "No Image"
    image_tag.short_description = 'Profile Image'
