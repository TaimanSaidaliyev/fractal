from django.shortcuts import render, redirect

from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout


def sing_in(request):
    if(request.user.is_authenticated):
        return redirect('home')
    else:
        template = 'start_page/sign_in.html'
        if request.method == 'POST':
            form = UserLoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('home')
        else:
            form = UserLoginForm()
        return render(request, template, {'form': form})


def user_logout(request):
    logout(request)
    return redirect('signin')

