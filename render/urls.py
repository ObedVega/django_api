from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/check/<path:url>/', views.check, name='check'),
]