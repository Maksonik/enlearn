from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import JsonResponse
from .models import StudyWord, Learner
from word.models import Word

import json

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

@csrf_exempt
def create_study_word(request):
    user = request.user
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        word = data['word']
    new_word = StudyWord.objects.create(learner=Learner.objects.get(user=user), word=Word.objects.get(name=word))
    new_word.save()
    return JsonResponse({'message': 'Данные успешно получены и обработаны.'})

@csrf_exempt
def check_study_word(request):
    user = request.user
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        word = data['word']
    try:
        obj = StudyWord.objects.get(learner=Learner.objects.get(user=user), word=Word.objects.get(name=word))
        return JsonResponse({'message': 'yes'})
    except StudyWord.DoesNotExist:
        return JsonResponse({'message': 'no'})


@csrf_exempt
def change_level_word(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        word = StudyWord.objects.get(word__name=data['word'])
        if data['level'] == 'up':
            next_stage = _increment_stage(word.stage_learning_word)
            word.stage_learning_word = next_stage
            word.save()
        elif data['level'] == 'down':
            prev_stage = _decrement_stage(word.stage_learning_word)
            word.stage_learning_word = prev_stage
            word.save()
        return JsonResponse({'message': 'Данные успешно получены и обработаны.'})
    else:
        return JsonResponse({'message': 'Метод не поддерживается.'}, status=405)




STAGE = (
    'Learning_0_stage',
    'Learning_1_stage',
    'Learning_2_stage',
    'Learning_3_stage',
    'Learning_4_stage',
    'Learning_5_stage',
    'Learned'
 )

def _increment_stage(current_stage):
    next_stage = STAGE.index(current_stage) + 1
    print(f'Incrementing stage: {current_stage} -> {STAGE[next_stage]}')
    return STAGE[next_stage]

def _decrement_stage(current_stage):
    prev_stage = STAGE.index(current_stage) - 1
    if prev_stage < 0:
        prev_stage = 0
    print(f'Decrementing stage: {current_stage} -> {STAGE[prev_stage]}')

    return STAGE[prev_stage]