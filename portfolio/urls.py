from django.urls import path
from .views import PortfolioViewSet

urlpatterns = [
    path('', PortfolioViewSet.as_view({'get': 'portfolio_view'}), name='portfolio'),
]
