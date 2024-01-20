from django.contrib import admin
from achieve.models import Achieve, AchieveLearner

@admin.register(Achieve)
class AchieveAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','image', )





@admin.register(AchieveLearner)
class AchieveLearnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'achievement','achievement_date')
