# Функции для достижение ачивок
from account.redis import _get_user_actions_for_all_days, _get_day


def _get_sum_learned_words(learner):
    """Получить число, общего количества выученных слов"""
    all_learned_words = learner.learning_word.filter(stage_learning_word='Learned')
    return len(all_learned_words)


def _get_consecutive_days_of_activity(learner):
    """Получить число, сколько дней подряд пользователь вёл активность"""
    all_days_with_activity = _get_user_actions_for_all_days(learner.user)
    consecutive_days_of_activity = 0
    day = _get_day()
    i = 0

    while day in all_days_with_activity and consecutive_days_of_activity < 365:
        consecutive_days_of_activity += 1
        i -= 1
        day = _get_day(i)

    return consecutive_days_of_activity


def _registration(learner):
    if learner:
        return True
    else:
        return False

def _study_100_words(learner):
    all_learned_words = _get_sum_learned_words(learner)
    return all_learned_words >= 100

def _study_500_words(learner):
    all_learned_words = _get_sum_learned_words(learner)
    return all_learned_words >= 500

def _study_1000_words(learner):
    all_learned_words = _get_sum_learned_words(learner)
    return all_learned_words >= 1000

def _study_2000_words(learner):
    all_learned_words = _get_sum_learned_words(learner)
    return all_learned_words >= 2000

def _study_5000_words(learner):
    all_learned_words = _get_sum_learned_words(learner)
    return all_learned_words >= 5000

def _study_10000_words(learner):
    all_learned_words = _get_sum_learned_words(learner)
    return all_learned_words >= 10000

def _weekly_site_activity(learner):
    consecutive_days_of_activity = _get_consecutive_days_of_activity(learner)
    return consecutive_days_of_activity >= 7

def _monthly_site_activity(learner):
    consecutive_days_of_activity = _get_consecutive_days_of_activity(learner)
    return consecutive_days_of_activity >= 30

def _yearly_site_activity(learner):
    consecutive_days_of_activity = _get_consecutive_days_of_activity(learner)
    return consecutive_days_of_activity >= 365

 # Словарь условий и соответствующих функций проверки
СONDITION_CHECK = {
    'registration': _registration,
    'study_100_words': _study_100_words,
    'study_500_words': _study_500_words,
    'study_1000_words': _study_1000_words,
    'study_2000_words': _study_2000_words,
    'study_5000_words': _study_5000_words,
    'study_10000_words': _study_10000_words,
    'weekly_site_activity': _weekly_site_activity,
    'monthly_site_activity': _monthly_site_activity,
    'yearly_site_activity': _yearly_site_activity,
}



