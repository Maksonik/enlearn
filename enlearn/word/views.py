from django.shortcuts import render
from word.models import Word

# Create your views here.
def WordDetail(request,title):
    word = Word.objects.get(title=title)
    return render(request,
                  'detail.html',
                  {'word' : word})