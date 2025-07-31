from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Portfolio
from .serializers import PortfolioSerializer
from drf_yasg.utils import swagger_auto_schema
from django.utils import translation


class PortfolioViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description='Get Home list with translation',
        responses={200: PortfolioSerializer(many=True)},
        tags=['portfolio'],
    )
    def portfolio_view(self, request):
        queryset = Portfolio.objects.all()
        serializer = PortfolioSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
