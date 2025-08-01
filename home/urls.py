from django.urls import path
from .views import HomeViewSet

urlpatterns = [
    path('', HomeViewSet.as_view({'get': 'home_view'}), name='portfolio'),
]
