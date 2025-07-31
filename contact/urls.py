from django.urls import path
from .views import HomeViewSet

urlpatterns = [
    path('get_contact_us/', HomeViewSet.as_view({'get': 'contact_us'}), name='get_contact_us'),
    path('get_why_choose_us/', HomeViewSet.as_view({'get': 'why_choose_us'}), name='get_why_choose_us'),
    path('post_contact/', HomeViewSet.as_view({'post': 'contact'}), name='post_contact'),
]
