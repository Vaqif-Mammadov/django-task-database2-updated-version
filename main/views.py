from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms

# def home_view(request):
#     return render(request, 'home.html')

def home(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()

    profiles = Profile.objects.all()
    return render(request, 'main/home.html', {'form': form, 'profiles': profiles})

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully logged in')
                return redirect('/')
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('/')
        else:
            messages.error(request, 'Registration failed. Please correct the error below.')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('/')
