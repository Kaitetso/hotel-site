from django.shortcuts import render
from .models import Client

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserLoginForm

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirect to login page
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('client_list')  # Redirect to client list or another page
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def client_list(request):
    clients = Client.objects.all()  # Убедитесь, что здесь нет фильтров
    return render(request, 'client_list.html', {'clients': clients})


from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Создаем запись в таблице clients
            Client.objects.create(
                first_name=user.first_name,
                last_name=user.last_name,
                email=user.email,
                phone_number=request.POST.get('phone_number')  # Если у вас есть соответствующее поле в форме
            )

            return redirect('login')  # Redirect to login page
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Здесь создадим шаблон home.html
