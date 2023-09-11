from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check/<path:url>/', views.check, name='check'),
    path('img/<path:main_url>/', views.check_img, name='check_img'),
    path('data/<str:api>/<str:ip>/<str:ciudad>/<str:estado>/<str:pais>/<str:loc>/', views.datos, name='datos'),
    path('datos/', views.consultar_archivo, name='consultar_archivo'),

]