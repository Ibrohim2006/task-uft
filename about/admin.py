from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import About


class AboutAdmin(TranslatableAdmin):
    list_display = ('get_name', 'get_description', 'image', 'created_at', 'updated_at')

    def get_name(self, obj):
        return obj.safe_translation_getter('name', any_language=True)

    def get_description(self, obj):
        return obj.safe_translation_getter('description', any_language=True)

    get_name.short_description = 'Name'
    get_description.short_description = 'Description'


admin.site.register(About, AboutAdmin)
