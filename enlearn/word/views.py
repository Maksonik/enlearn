from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Word
from .serializers import WordSerializer


@csrf_exempt
def word_detail(request, name):
    '''
    Информация о слове
    '''
    try:
        word = Word.objects.get(name=name)
    except Word.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = WordSerializer(word)
        return render(request,
                      'detail.html',
                      {'word': serializer.data})


class WordViewSet(viewsets.ModelViewSet):
    '''
    Представление модуля Word через API
    '''

    queryset = Word.objects.all()
    serializer_class = WordSerializer
    # permission_classes = [IsAdminUser]
    lookup_field = 'name'

