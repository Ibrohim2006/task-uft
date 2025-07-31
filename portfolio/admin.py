from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(TranslatableAdmin):
    list_display = ('translated_name', 'translated_description', 'image', 'created_at', 'updated_at')

    def translated_name(self, obj):
        return obj.safe_translation_getter('name', any_language=True)

    def translated_description(self, obj):
        return obj.safe_translation_getter('description', any_language=True)

    translated_name.short_description = 'Name'
    translated_description.short_description = 'Description'
