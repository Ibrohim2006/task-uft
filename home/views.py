from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Home
from .serializers import HomeSerializer
from drf_yasg.utils import swagger_auto_schema
from django.utils import translation


class HomeViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description='Get Home list with translation',
        responses={200: HomeSerializer(many=True)},
        tags=['Home'],
    )
    def home_view(self, request):
        queryset = Home.objects.all()
        serializer = HomeSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
