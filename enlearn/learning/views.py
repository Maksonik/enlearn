from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from account.models import StudyWord, Learner
from word.models import Word
from achieve.models import AchieveLearner, Achieve
from datetime import datetime
from account.views import get_user_actions_for_all_days
import json
import pytz
from achieve.views import set_new_achieves_for_user

def profile(request):
    user = request.user
    set_new_achieves_for_user(request)
    activity = get_user_actions_for_all_days(user)
    study_word_count_for_stage = get_study_word_count_for_stage(user)
    user_achieves = AchieveLearner.objects.filter(user=Learner.objects.get(user=user))
    all_achieves = Achieve.objects.all()
    achieves_unreceived = all_achieves.exclude(id__in=user_achieves.values_list('achievement__id', flat=True))
    return render(request,
                  'profile/profile.html',
                  {'user' : user,
                   'activity' : activity,
                   'study_words': study_word_count_for_stage,
                   'user_achieves':user_achieves,
                   'achieves_unreceived' : achieves_unreceived})
    
def get_study_word_count_for_stage(user):
    words = StudyWord.objects.filter(learner__user=user)
    return {'Слова на 1 этапе' : len(words.filter(stage_learning_word='Learning_0_stage')),
            'Слова на 2 этапе' : len(words.filter(stage_learning_word='Learning_1_stage')),
            'Слова на 3 этапе' : len(words.filter(stage_learning_word='Learning_2_stage')),
            'Слова на 4 этапе' : len(words.filter(stage_learning_word='Learning_3_stage')),
            'Слова на 5 этапе' : len(words.filter(stage_learning_word='Learning_4_stage')),
            'Слова на 6 этапе' : len(words.filter(stage_learning_word='Learning_5_stage')),
            'Выучено слов' : len(words.filter(stage_learning_word='Learned')),
            'Всего слов' : len(words)}


def exercises(request):
    all_words = Word.objects.order_by('rank')
    learning_words = StudyWord.objects.filter(learner__user=request.user)
    remaining_words = all_words.exclude(id__in=learning_words.values_list('word', flat=True))[:100]
    return render(request,
                  'exercises.html',
                  {'words': remaining_words})
    
def remember_all(request):
    return render(request,
                  'exercises/remember_all.html')

def biathlon(request):
    return render(request,
                  'exercises/biathlon.html') 

def get_all_studywords(request):
    """ Выгружает всё слова, которые нужно сегодня повторить """
    user = request.user
    words = StudyWord.objects.filter(learner__user=user,
                                     time_learning__lt=pytz.timezone('Europe/Moscow').localize(datetime.now()))
    words_data = json.dumps(list(words.values()), cls=DjangoJSONEncoder)
    return JsonResponse({'data' : words_data}, content_type='application/json', safe=False)
