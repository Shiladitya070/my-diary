from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .form import UserSignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.urls import reverse


def register(request):
    if request.method == 'POST':
        if User.objects.filter(email=request.POST.get('email')).exists():
            messages.error(request, f'email already exists!')
            return redirect('register')
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            messages.success(
                request, f'Resgistration done')
            return redirect('login')
    else:
        form = UserSignUpForm()
    return render(request, 'users/register.html', {'form': form})




def llogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                print('TEST')
                messages.info(request, 'Inactive user')
                return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, 'Invalid username/password!')
        return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'users/login.html', {})


