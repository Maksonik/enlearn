from django.db import models
from django.contrib.auth.models import User
from word.models import Word
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import timedelta,datetime


DAYS = {
    'Learning_0_stage': 0,
    'Learning_1_stage': 1,
    'Learning_2_stage': 3,
    'Learning_3_stage': 7,
    'Learning_4_stage': 15,
    'Learning_5_stage': 30,
}


class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class StudyWord(models.Model):
    word = models.ForeignKey(Word, related_name='learning_word',on_delete=models.CASCADE)
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    stage_learning_word = models.CharField(choices=[
        ('Learning_0_stage', 'Learning_0_stage'),
        ('Learning_1_stage', 'Learning_1_stage'),
        ('Learning_2_stage', 'Learning_2_stage'),
        ('Learning_3_stage', 'Learning_3_stage'),
        ('Learning_4_stage', 'Learning_4_stage'),
        ('Learning_5_stage', 'Learning_5_stage'),
        ('Learned', 'Learned'),
    ], default='Learning_0_stage')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    time_learning = models.DateTimeField(null=True)
    
    class Meta:
        unique_together = ('word', 'learner')


@receiver(pre_save, sender=StudyWord)
def update_time_learning(sender, instance, **kwargs):
    print('update_time_learning signal triggered')
    if not instance.id:
        instance.time_learning = datetime.now()
    else:
        if instance.stage_learning_word == 'Learned':
            instance.time_learning = None
        else:
            instance.time_learning = instance.updated + timedelta(days=DAYS[instance.stage_learning_word])

pre_save.connect(update_time_learning, sender=StudyWord)