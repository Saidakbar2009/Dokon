from django.urls import path
from .views import *

urlpatterns = [
    path('asosiy/', asosiy),
    path('asosiy2/', asosiy2),
    path('BolimlarView/', BolimlarView),
    path('MahsulotlarView/', MahsulotlarView),
    path('MahsulotView/', MahsulotView),
]