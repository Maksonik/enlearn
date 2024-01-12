from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
import json
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Word, Example
from .serializers import WordSerializer, ExampleSerializer


def word_detail(request):
    """Сайт для детального обзора страницы"""
    word_name = request.GET.get('word')
    try:
        word = get_object_or_404(Word, name=word_name.lower().strip())
        if request.method == 'GET':
            serializer = WordSerializer(word)
            word = serializer.data
            descriptions = _get_description(word)
            forms = _get_form(word)
            return render(request, 'detail.html',
                        {'word': word,
                        'descriptions': descriptions,
                        'forms' : forms})
    except Http404:
        return render(request,
                      'mistake.html')
        

def _get_description(word):
    """Собрать descriptions для облегченной работы в htnl"""
    descriptions = {}
    for desc in word['descriptions']:
        descriptions.setdefault(desc['part_of_speech'], {})
        descriptions[desc['part_of_speech']].setdefault(
            desc['general_meaning'], [])
        descriptions[desc['part_of_speech']][desc['general_meaning']].append(
            (desc['deep_meaning'], desc['translate']))
    return descriptions

def _get_form(word):
    """Собрать forms для облегченной работы в htnl"""
    forms = {}
    for form in word['forms']:
         forms.setdefault(form['part_of_speech'], [])
         forms[form['part_of_speech']].append([form['condition'],form['value']])
    return forms


def word_list(request):
    """Для поисковой страницы"""
    if request.method == 'GET':
        text = request.GET.get('text', '')
        if text == '':
            return JsonResponse({'success': True, 'words': ''})

        words = Word.objects.filter(name__startswith=text)
        directory = _get_dict_filtered_words(words)
        try:
            return JsonResponse({'success': True, 'words': directory})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

def _get_dict_filtered_words(words):
    """Получить словарь нужных нам слов"""
    directory = []
    for word in words:
        directory.append(
            {'name': word.name, 'short_description': word.short_description})
    return directory

class WordViewSet(viewsets.ModelViewSet):
    """Представление модуля Word через API"""

    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [IsAdminUser]



class ExampleViewSet(viewsets.ModelViewSet):
    """Представление модуля Word через API"""

    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
    # permission_classes = [IsAdminUser]


