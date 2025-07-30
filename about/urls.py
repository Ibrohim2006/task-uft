from django.urls import path
from .views import AboutView

urlpatterns = [
    path('', AboutView.as_view({'get': 'about_view'}), name='about'),
]
