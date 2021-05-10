from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .form import UserRegisterFrom, UserUpdatedForm, UserSignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import login, authenticate
from django.views import View
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


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success('Your account has been activate successfully')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid!')
        return redirect('home')


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


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdatedForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdatedForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'users/profile.html', context)
