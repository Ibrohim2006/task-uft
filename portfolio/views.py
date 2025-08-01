from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Portfolio
from .serializers import PortfolioSerializer
from drf_yasg.utils import swagger_auto_schema


class PortfolioViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description='Get portfolio list with translation',
        responses={200: PortfolioSerializer(many=True)},
        tags=['Portfolio'],
    )
    def portfolio_view(self, request):
        portfolios = Portfolio.objects.all()
        serializer = PortfolioSerializer(portfolios, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
