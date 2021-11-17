from django.urls import path
from . import views

urlpatterns = [
    path('', views.TopView.as_view(),),
    path('api/<int:pk>/', views.WeatherAPIView.as_view()),
]
