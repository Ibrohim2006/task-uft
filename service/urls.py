from django.urls import path
from .views import HomeViewSet

urlpatterns = [
    path('get_services/', HomeViewSet.as_view({'get': 'services'}), name= 'get_services'),
    path('get_technologys/', HomeViewSet.as_view({'get': 'technologys'}), name= 'get_technologys'),

]