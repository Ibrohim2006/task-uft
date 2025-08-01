from django.utils.translation import get_language
from rest_framework import serializers
from .models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.safe_translation_getter('name', language_code=get_language())

    def get_description(self, obj):
        return obj.safe_translation_getter('name', language_code=get_language())

    class Meta:
        model = Portfolio
        fields = ('id', 'name', 'description', 'image', 'created_at', 'updated_at')
