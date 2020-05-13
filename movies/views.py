from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie

# Create your views here.

def index(request):
    return render(request, 'main.html')

# 영화추가삭제 ==> 관리자만 (admin page에서 관리)