from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import JsonResponse
from django.conf import settings
from .models import StudyWord, Learner
from word.models import Word


from datetime import datetime, timedelta
import redis
import json
import pytz

r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)

def increment_learner_action(user, action, expiration_days=365):
    day = _get_day()
    key = f'user:{user}:{day}'
    r.hincrby(key,action,1)
    r.expire(key, expiration_days * 24 * 60 * 60)
    
def get_user_actions_for_day(user_id, day):
    key = f"user:{user_id}:{day}"
    stored_data = r.hgetall(key)
    if stored_data:
        return {field.decode("utf-8"): int(value) for field, value in stored_data.items()}
    return None

def get_user_actions_for_all_days(user):
    pattern = f"user:{user}:*"
    keys = r.keys(pattern)
    
    result = {}
    
    for key in keys:
        stored_data = r.hgetall(key)
        day = key.decode("utf-8").split(":")[-1]
        
        if stored_data:
            result[day] = {field.decode("utf-8"): int(value) for field, value in stored_data.items()}

    return result if result else None
    
def _get_day(offset=0):
    now_in_moscow = pytz.timezone('Europe/Moscow').localize(datetime.now())
    previous_day = now_in_moscow - timedelta(days=abs(offset))
    return previous_day.strftime("%Y-%m-%d")

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
    increment_learner_action(user, 'start_learning_word')
    return JsonResponse({'message': 'Данные успешно получены и обработаны.'})

@csrf_exempt
def check_study_word(request):
    user = request.user
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        word = data['word']
    try:
        message = {'message': 'yes'}
        obj = StudyWord.objects.get(learner=Learner.objects.get(user=user), word=Word.objects.get(name=word))
        if obj.stage_learning_word == 'Learned':
            message['learning'] = 'yes'
        else:
            message['learning'] = 'no'
        return JsonResponse(message)
    except StudyWord.DoesNotExist:
        message = {'message': 'no'}
        return JsonResponse(message)


@csrf_exempt
def change_level_word(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        word = StudyWord.objects.get(word__name=data['word'])
        if data['level'] == 'up':
            next_stage = _increment_stage(word.stage_learning_word)
            word.stage_learning_word = next_stage
            word.save()
            increment_learner_action(request.user,f'up to {next_stage}')
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
    return STAGE[next_stage]

def _decrement_stage(current_stage):
    prev_stage = STAGE.index(current_stage) - 1
    if prev_stage < 0:
        prev_stage = 0
    return STAGE[prev_stage]