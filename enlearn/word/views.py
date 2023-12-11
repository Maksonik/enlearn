from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Word, Example
from .serializers import WordSerializer, ExampleSerializer



def word_detail(request):
    word_name = request.GET.get('word')
    word = get_object_or_404(Word, name=word_name.lower())

    if request.method == 'GET':
        serializer = WordSerializer(word)
        descriptions = {}
        word = serializer.data
        for desc in word['descriptions']:
           descriptions.setdefault(desc['part_of_speech'], {})
           descriptions[desc['part_of_speech']].setdefault(desc['general_meaning'], [])
           descriptions[desc['part_of_speech']][desc['general_meaning']].append((desc['deep_meaning'], desc['translate']))
        return render(request, 'detail.html', 
                      {'word': word,
                       'descriptions' : descriptions})


class WordViewSet(viewsets.ModelViewSet):
    '''
    Представление модуля Word через API
    '''

    queryset = Word.objects.all()
    serializer_class = WordSerializer
    # permission_classes = [IsAdminUser]
    lookup_field = 'name'

class ExampleViewSet(viewsets.ModelViewSet):
    '''
    Представление модуля Word через API
    '''

    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
    # permission_classes = [IsAdminUser]


