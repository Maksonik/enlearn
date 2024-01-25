# Работа с ачивками
from django.contrib import messages

from account.models import Learner
from achieve.achievements import СONDITION_CHECK
from achieve.models import AchieveLearner, Achieve


def _check_achieve(learner,achieve):
    """Проверить на выполненные достижения пользователем"""
    condition_key = achieve.condition
    if condition_key in СONDITION_CHECK:
        return СONDITION_CHECK[condition_key](learner)
    else:
        return False

def _set_new_achieves_for_user(request):
    """Установить новые выполненные достижения"""
    learner = Learner.objects.get(user=request.user)
    user_achieves = AchieveLearner.objects.filter(user=learner)
    all_achieves = Achieve.objects.all()
    achieves_unreceived = all_achieves.exclude(id__in=user_achieves.values_list('achievement__id', flat=True))
    for achieve in achieves_unreceived:
        if _check_achieve(learner, achieve):
            AchieveLearner.objects.create(user=learner, achievement=achieve)
            messages.success(request, f'Получено достижение {achieve}')

