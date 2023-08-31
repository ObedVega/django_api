from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/check/<path:url>/', views.check, name='check'),
    path('api/img/<path:main_url>/', views.check_img, name='check_img'),
]