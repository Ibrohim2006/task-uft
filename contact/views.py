from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ViewSet
from .models import ContactUsModel, WhyChooseUsModel, ContactModel
from .serializers import ContactUsSerializer, WhyChooseUsSerializer, ContactSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

class HomeViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description='Get ContactUs list with translation',
        responses={200: ContactUsSerializer(many=True)},
        tags=['ContactUs']
    )
    def contact_us(self, request, *args, **kwargs):
        contact_us = ContactUsModel.objects.first()
        serializer = ContactUsSerializer(contact_us, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description='Get WhyChooseUs list with translation',
        responses={200: WhyChooseUsSerializer(many=True)},
        tags=['WhyChooseUs']
    )
    def why_choose_us(self, request, *args, **kwargs):
        why_choose_us = WhyChooseUsModel.objects.all()
        serializer = WhyChooseUsSerializer(why_choose_us, many=True, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(request_body=ContactSerializer,
                         responses={201: ContactSerializer, 400: 'Bad Request'})
    def contact(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
