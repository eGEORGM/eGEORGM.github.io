from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Category
 
def hangye(request):
    return render(request,'chongsheng.html')
def quyu(request):
    return render(request,'weiyue.html')