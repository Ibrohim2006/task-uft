from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Home


@admin.register(Home)
class HomeAdmin(TranslatableAdmin):
    list_display = ('translation_name', 'translation_description', 'image', 'created_at', 'updated_at')

    def translation_name(self, obj):
        return obj.safe_translation_getter('name', any_language=True)

    def translation_description(self, obj):
        return obj.safe_translation_getter('description', any_language=True)
