from django.urls import path
from .views import PingPongView

urlpatterns = [
    path('ping/', PingPongView.as_view(), name='ping'),
]
