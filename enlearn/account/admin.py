from django.contrib import admin
from .models import Learner, StudyWord


class StudyWordInline(admin.TabularInline):
    model = StudyWord
    extra = 1
    raw_id_fields = ('word',)
    readonly_fields = ('created', 'updated','time_learning')


@admin.register(Learner)
class LearnerAdmin(admin.ModelAdmin):
    list_display = ('user',)
    inlines = [StudyWordInline]

