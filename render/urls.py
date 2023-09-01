from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check/<path:url>/', views.check, name='check'),
    path('img/<path:main_url>/', views.check_img, name='check_img'),
]