from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm


User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, '다시 입력해주세요.')

    form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'users/signup.html', context)


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
        else:
            messages.error(request, '잘못된 회원정보입니다.')
    
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/signin.html', context)


@login_required
def signout(request):
    logout(request)
    return redirect('index')


def detail(request, username):
    person = get_object_or_404(User, username=username)
    context = {
        'person': person,
    }
    return render(request, 'users/detail.html', context)


@login_required
def follow(request, user_pk):
    user = request.user
    person = get_object_or_404(User, pk=user_pk)

    if person in user.followings:
        user.followings.remove(person)
    else:
        user.followings.add(person)
    
    return redirect('user_detail')