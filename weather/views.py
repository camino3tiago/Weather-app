from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import WeatherSerializer
from .models import Weather

class TopView(ListView):
    model = Weather
    template_name = 'top.html'

class WeatherAPIView(RetrieveAPIView):  # RetrieveAPIViewは個別の情報を取得するViewのため、パスにpk等の設定が必須
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
    permission_classes = [IsAuthenticated]