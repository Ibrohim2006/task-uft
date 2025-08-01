from rest_framework import serializers
from .models import Home


class HomeSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.safe_translation_getter('name', any_language=True)

    def get_description(self, obj):
        return obj.safe_translation_getter('description', any_language=True)

    class Meta:
        model = Home
        fields = ('id', 'name', 'description', 'image', 'created_at', 'updated_at')
