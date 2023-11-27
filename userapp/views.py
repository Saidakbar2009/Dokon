import random

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from random import *
from eskiz.client import SMSClient
from django.conf import settings
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username = request.POST.get('username'),
            password = request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('/')
    return render(request, 'page-user-login.html')

def RegisterView(request):
    if request.method == 'POST':
        profil = Profil.objects.create_user(
            username=request.POST.get('t'),
            first_name=request.POST.get('f'),
            last_name=request.POST.get('l'),
            password=request.POST.get('p'),
            tel=request.POST.get('t'),
            shahar=request.POST.get('sh'),
            davlat=request.POST.get('d'),
            jins=request.POST.get('gender'),
            tasdiqlash_kodi=str(randrange(10000, 100000))
        )
        mijoz = SMSClient(
            api_url="https://notify.eskiz.uz/api/",
            email=settings.EMAIL,
            password=settings.P,
        )
        mijoz._send_sms(
            phone_number=profil.tel,
            message=f'Dokon uchun tasdiqlash kodiz: {profil.tasdiqlash_kodi}'
        )
        login(request, profil)
        return redirect('/userapp/tasdiqlash')
    return render(request, 'page-user-register.html')

def KodTasdiqlash(request):
    if request.method == 'POST':
        profil = Profil.objects.get(id=request.user.id)
        if profil.tasdiqlash_kodi == request.POST.get('k'):
            profil.tasdiqlangan = True
            profil.save()
            return redirect('/asosiy/asosiy')
        return redirect('/userapp/tasdiqlash/')
    return render(request, 'tasdiqlash.html')