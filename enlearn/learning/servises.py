# Работа с данными
import json
from datetime import datetime
import re
import pytz

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q, IntegerField
from django.db.models.functions import Cast

from account.models import StudyWord
from word.models import Word


def _get_study_word_count_for_stage(user):
    """Вывод данных для статистики на странице profile.html"""
    words = StudyWord.objects.filter(learner__user=user)
    return {'Слова на 1 этапе': len(words.filter(stage_learning_word='Learning_0_stage')),
            'Слова на 2 этапе': len(words.filter(stage_learning_word='Learning_1_stage')),
            'Слова на 3 этапе': len(words.filter(stage_learning_word='Learning_2_stage')),
            'Слова на 4 этапе': len(words.filter(stage_learning_word='Learning_3_stage')),
            'Слова на 5 этапе': len(words.filter(stage_learning_word='Learning_4_stage')),
            'Слова на 6 этапе': len(words.filter(stage_learning_word='Learning_5_stage')),
            'Выучено слов': len(words.filter(stage_learning_word='Learned')),
            'Всего слов': len(words)}


def _words_for_exercises(user):
    """Выдать 100 слов, которые можно начать учить"""
    #FIXME: переделать модель Word, а то ужас какой-то
    all_words = Word.objects.exclude(Q(rank='0') | Q(rank__regex=r'\D'))
    all_words = all_words.annotate(rank_as_int=Cast('rank', output_field=IntegerField()))
    all_words = all_words.order_by('rank_as_int')
   
    learning_words = StudyWord.objects.filter(learner__user=user)
    remaining_words = all_words.exclude(id__in=learning_words.values_list('word', flat=True))[:100]
    return remaining_words


def _get_all_studywords(user):
    """Получить слова, которые нужно сегодня выучить"""
    words = StudyWord.objects.filter(learner__user=user,
                                     time_learning__lt=pytz.timezone('Europe/Moscow').localize(datetime.now()))
    words_data = json.dumps(list(words.values()), cls=DjangoJSONEncoder)
    return words_data

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
    """Увеличить этап изучаемого слова на один"""
    next_stage = STAGE.index(current_stage) + 1
    return STAGE[next_stage]


def _decrement_stage(current_stage):
    """Уменьшить этап изучаемого слова на один"""
    prev_stage = STAGE.index(current_stage) - 1
    if prev_stage < 0:
        prev_stage = 0
    return STAGE[prev_stage]
