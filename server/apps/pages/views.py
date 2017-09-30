from django.shortcuts import render, redirect
# from django.template import Context, Template
# from rest_framework.authtoken.models import Token
# from apps.users.models import Profile

def home(request):
    return render(request, 'index.html')