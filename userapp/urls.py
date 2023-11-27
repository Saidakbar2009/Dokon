from django.urls import path
from .views import *

urlpatterns = [
    path('login', login_view),
    path('register/', RegisterView),
    path('tasdiqlash/', KodTasdiqlash)
]