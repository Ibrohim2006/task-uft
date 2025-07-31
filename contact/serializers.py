from django.conf import settings
from rest_framework import serializers
from .models import ContactUsModel, WhyChooseUsModel, ContactModel


class ContactUsSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)

    def get_description(self, obj):
        return obj.safe_translation_getter('description', any_language=True)

    class Meta:
        model = ContactUsModel
        fields = ['id', 'title', 'description']



class WhyChooseUsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    def get_name(self, obj):
        return obj.safe_translation_getter('name', any_language=True)

    class Meta:
        model = WhyChooseUsModel
        fields = ['id', 'name']



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ['id', 'fullname', 'surname', 'email', 'company_name', 'phone_number', 'description']