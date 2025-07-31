from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import OurServicesModel, OurTechnologyModel


@admin.register(OurServicesModel)
class OurServicesAdmin(TranslatableAdmin):
    list_display = ('get_title', 'get_name', 'get_title2', 'get_name2', 'get_description')

    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)

    def get_name(self, obj):
        return obj.safe_translation_getter('name', any_language=True)

    def get_title2(self, obj):
        return obj.safe_translation_getter('title2', any_language=True)

    def get_name2(self, obj):
        return obj.safe_translation_getter('name2', any_language=True)

    def get_description(self, obj):
        return obj.safe_translation_getter('description', any_language=True)


@admin.register(OurTechnologyModel)
class OurTechnologyAdmin(TranslatableAdmin):
    list_display = ('get_title', 'get_name')
    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)

    def get_name(self, obj):
        return obj.safe_translation_getter('name', any_language=True)