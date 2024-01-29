from django.contrib import admin
from .models import Learner, StudyWord
from achieve.models import AchieveLearner


class AchieveLearnerInline(admin.TabularInline):
    model = AchieveLearner
    extra = 1
    readonly_fields = ('user', 'achievement', 'achievement_date')


class StudyWordInline(admin.TabularInline):
    model = StudyWord
    extra = 1
    raw_id_fields = ('word',)
    readonly_fields = ('created', 'updated', 'time_learning')


@admin.register(Learner)
class LearnerAdmin(admin.ModelAdmin):
    list_display = ('user',)
    inlines = [AchieveLearnerInline, StudyWordInline]
