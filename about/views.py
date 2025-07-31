from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import About
from .serializers import AboutSerializer
from drf_yasg.utils import swagger_auto_schema
from django.utils import translation


class AboutView(ViewSet):
    @swagger_auto_schema(
        operation_description='About list',
        responses={200: AboutSerializer(many=True)},
        tags=['About'],
    )
    def about_view(self, request):

        about = About.objects.all()
        serializer = AboutSerializer(about, many=True, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)