from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def home(request):
    return render(request, 'eccentric/home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'eccentric/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        print('post')
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # print(password, username)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('clients:index')
            else:
                print('not user')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'eccentric/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')