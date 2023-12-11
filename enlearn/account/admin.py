from django.contrib import admin
from .models import Learner

@admin.register(Learner)
class LearnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'word', 'stage_learning_word', 'created', 'updated']


