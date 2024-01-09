from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from account.models import StudyWord
from word.models import Word
from word.serializers import WordSerializer
from datetime import datetime
import json
import pytz


def profile(request):
    return render(request,
                  'profile/profile.html')


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


    

def finished(request):
    return render(request,
                  'exercises/finished.html')