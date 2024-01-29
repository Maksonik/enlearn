import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .services import _get_description, _get_form, _get_dict_words_with_short_description
from .models import Word, Example
from .serializers import WordSerializer, ExampleSerializer


def word_detail(request):
    """Страница для детального обзора слова"""
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
                           'forms': forms})
    except Http404:
        return render(request,
                      'mistake.html')


def word_list(request):
    """Cписок слов по запрошенной подстроки"""
    if request.method == 'GET':
        text = request.GET.get('text', '').strip().lower()
        if text == '':
            return JsonResponse({'error': 'Nothing transferred', 'words': ''})

        words = Word.objects.filter(name__startswith=text)
        directory = _get_dict_words_with_short_description(words)
        try:
            return JsonResponse({'success': True, 'words': directory})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


class WordViewSet(viewsets.ModelViewSet):
    """Представление модуля Word через API"""

    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [IsAdminUser]


class ExampleViewSet(viewsets.ModelViewSet):
    """Представление модуля Example через API"""

    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
    permission_classes = [IsAdminUser]
