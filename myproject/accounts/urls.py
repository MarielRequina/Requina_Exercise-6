# urls.py
from django.urls import path
from .views import RegisterAPIView, LoginAPIView

urlpatterns = [
    path('api/register/', RegisterAPIView.as_view(), name='register'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
]
