from rest_framework import serializers
from .models import About


class AboutSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = About
        fields = ('id', 'name', 'description', 'image', 'created_at', 'updated_at')

    def get_name(self, obj):
        return obj.safe_translation_getter('name', any_language=True)

    def get_description(self, obj):
        return obj.safe_translation_getter('description', any_language=True)
