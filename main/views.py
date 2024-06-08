from django.shortcuts import render, redirect, HttpResponse
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import LoginForm,RegisterForm
from django.template import loader
import pdfkit


path_wkthmltopdf = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'

config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)


# def home_view(request):
#return render(request, 'home.html')

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


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Giriş edildi')
                return redirect('/')
            else:
                messages.error(request, 'Belə bir istifadəçi yoxdur')
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
            messages.success(request, 'Qeydiyyat tamamlandı')
            return redirect('/')
        else:
            messages.error(request, 'Qeydiyyat uğursuz oldu. Zəhmət olmasa təkrar cəhd edin.')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Hesabdan çıxış edildi')
    return redirect('/')

def list_view(request):
    lists=Profile.objects.all()
    return render (request,'main/person_list.html',{'lists':lists})


def detail_view(request, id):
    user_profile = Profile.objects.get(id=id)
    template = loader.get_template("main/resume.html")
    html = template.render({"user_profile": user_profile})
    options = {"page-size": "Letter","encoding": "UTF-8"}
    pdf = pdfkit.from_string(html, False, options,configuration=config)
    response = HttpResponse(pdf, content_type="application/pdf")
    response['Content-Disposition'] = f'attachment; filename="download.pdf"'
    return response


