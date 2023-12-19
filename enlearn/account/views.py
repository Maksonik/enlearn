from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


def view_base(request):
    return render(request,
                  'base.html', )

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')  # Замените 'home' на имя вашей домашней страницы
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

