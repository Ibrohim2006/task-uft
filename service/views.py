from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ViewSet
from .models import OurServicesModel, OurTechnologyModel
from .serializers import OurServicesSerializer, OurTechnologySerializer
from rest_framework.response import Response
from rest_framework import status



class HomeViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description='Get Service list with translation',
        responses={200: OurServicesSerializer(many=True)},
        tags=['Services']
    )
    def services(self, request, *arg, **kwargs):
        services = OurServicesModel.objects.all().first()
        serializer = OurServicesSerializer(services, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description='Get Technology list with translation',
        responses={200: OurServicesSerializer(many=True)},
        tags=['Technology']
    )
    def technologys(self, request, *arg, **kwargs):
        technologys = OurTechnologyModel.objects.all().first()
        serializer = OurTechnologySerializer(technologys, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)