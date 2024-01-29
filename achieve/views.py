from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from account.models import Learner
from .models import Achieve, AchieveLearner
from .serveses import _set_new_achieves_for_user


@login_required
def list_achieve(request):
    user = request.user
    _set_new_achieves_for_user(request)
    user_achieves = AchieveLearner.objects.filter(user=Learner.objects.get(user=user))
    all_achieves = Achieve.objects.all()
    achieves_unreceived = all_achieves.exclude(id__in=user_achieves.values_list('achievement__id', flat=True))
    return render(request,
                  'list_achieve.html',
                  {'user_achieves': user_achieves,
                   'achieves_unreceived': achieves_unreceived})



