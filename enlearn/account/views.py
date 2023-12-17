from django.shortcuts import render


def view_base(request):
    return render(request,
                  'base.html', )
