from django.shortcuts import render



# Create your views here.

def view_base(request):
    return render(request,
                  'base.html', )
