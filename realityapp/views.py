# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as loginn, logout
from .utils import grecaptcha_verify
from models import call_us as calll

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']
        user = User(email=email, username=username)
        user.set_password(password)
        if not grecaptcha_verify(request):
            context = {'message_bad':'.لطفا تست روبات را کامل کنید'}
        elif User.objects.filter(email=request.POST['email']).exists():
            context = {'message_bad':'.این پست الکتونیکی قبلا استفاده شده است'}
        elif not password == password1:
            context = {'message_bad':'.کلمه عبور با هم مطابقت ندارد'}
        elif not User.objects.filter(username=request.POST['username']).exists():
            user.save()
            context = {'message_good':'.ثبت نام با موفقیت انجام شد'}
        else:
            context = {'message_bad':'.این نام کاربری قبلا استفاده شده است'}
    else:
        context = {}
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if not grecaptcha_verify(request):
            context = {'message_bad':'.لطفا تست روبات را کامل کنید'}
        elif user is not None:
            loginn(request, user)
            return redirect('/account/')
        else:
            context = {'message_bad':'.کلمه عبور یا نام کاربری اشتباه است'}
    else:
        context = {}
    return render(request, 'login.html',context)

def logoutt(request):
    logout(request)
    return redirect('/account/login/')

def account(request):
    return render(request, 'account.html')

def about_us(request):
    return render(request, 'about_us.html')

def call_us(request):
    if request.method == 'POST':
        if not grecaptcha_verify(request):
            context = {'message_bad':'.لطفا تست روبات را کامل کنید'}
        else:
            name = request.POST['name']
            email = request.POST['email']
            phonenumber = request.POST['phonenumber']
            content = request.POST['content']
            call = calll(name=name, email=email, phonenumber=phonenumber, content=content)
            call.save()
        context = {'message_good':'باتشکر, پیام شما باموفقیت ارسال شد.'}
    else:
        context = {}
    return render(request, 'call_us.html',context)
