from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import ContactUsModel, WhyChooseUsModel, ContactModel

@admin.register(ContactUsModel)
class ContactUsAdmin(TranslatableAdmin):
    list_display = ('get_title', 'get_description')

    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)

    def get_description(self, obj):
        return obj.safe_translation_getter('description', any_language=True)


@admin.register(WhyChooseUsModel)
class WhyChooseUsAdmin(TranslatableAdmin):
    list_display = ('get_name',)

    def get_name(self, obj):
        return obj.safe_translation_getter('name', any_language=True)


admin.site.register(ContactModel)
