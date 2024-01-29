from django.db import models
from account.models import Learner


class Achieve(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='achieve/', blank=True, null=True)
    condition = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class AchieveLearner(models.Model):
    user = models.ForeignKey(Learner, related_name='achieves', on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achieve, related_name='achieves', on_delete=models.CASCADE)
    achievement_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.achievement.title
