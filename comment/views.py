from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import Comment
from .serializers import CommentSerializer 
from parler.utils.context import switch_language
from rest_framework.parsers import MultiPartParser, FormParser
from drf_yasg import openapi
from django.utils import translation
from django.shortcuts import get_object_or_404
# Create your views here.

class CommentViewSet(ViewSet):
    parser_classes = (MultiPartParser, FormParser)

    @swagger_auto_schema(
        operation_description="Create a new comment",
        request_body=CommentSerializer,
        manual_parameters=[
            openapi.Parameter(
                'language_code',
                openapi.IN_FORM,
                description="Optional language code (e.g. 'en', 'ru')",
                type=openapi.TYPE_STRING
            )
        ],
        responses={201: CommentSerializer()}
    )
    def create(self, request):
        lang = request.data.get('language_code', 'en')
        # Create an unsaved instance to work in the desired language context.
        instance = Comment()
        with switch_language(instance, lang):
            serializer = CommentSerializer(instance=instance, data=request.data)
            if serializer.is_valid():
                instance = serializer.save()  # This saves in the 'lang' context.
                return Response(CommentSerializer(instance).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def list(self, request):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        lang = translation.get_language()
        with switch_language(comment, lang):
            serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
