from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from new.models import AddProduct
# Create your views here.
def home(request):
    return render(request, 'home.html')