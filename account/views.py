from django.shortcuts import render, redirect
from django.contrib.auth import login

from .models import Learner
from .forms import UserRegisterForm


def view_base(request):
    return render(request,
                  'base.html', )


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Learner.objects.create(user=user)
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
