from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    job = serializers.CharField()
    company = serializers.CharField(allow_blank=True, required=False)
    comment = serializers.CharField()
    profile_image = serializers.ImageField(required=False)
    feedback_file = serializers.FileField(required=False)
    
    class Meta:
        model = Comment
        fields = [
            'first_name',
            'last_name',
            'job',
            'company',
            'comment',
            'profile_image',
            'feedback_file',
        ]
