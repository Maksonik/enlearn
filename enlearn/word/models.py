from django.db import models
from django.contrib.auth.models import User

def sound_path(instance,filename):
    return f'sounds/{instance.word}/{instance.region}/{filename}'


class Word(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=1000)
    rank = models.CharField(default='20000')

    class Meta:
        ordering = ['name', 'rank']

    def __str__(self):
        return self.name


class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)

    stage_learning_word = models.CharField(choices=[
        ('Unknown', 'Unknown'),
        ('Learning_0_stage', 'Learning_0_stage'),
        ('Learning_1_stage', 'Learning_1_stage'),
        ('Learning_2_stage', 'Learning_2_stage'),
        ('Learning_3_stage', 'Learning_3_stage'),
        ('Learning_4_stage', 'Learning_4_stage'),
        ('Learning_5_stage', 'Learning_5_stage'),
        ('Learned', 'Learned'),
    ], default='Unknown')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Description(models.Model):
    word = models.ForeignKey(Word,
                             related_name='descriptions',
                             on_delete=models.CASCADE)
    part_of_speech = models.CharField(choices=[
        ('adjectival', 'Adjectival'),
        ('noun', 'Noun'),
        ('verb', 'Verb'),
    ])
    meaning = models.CharField(max_length=255, blank=True)
    translate = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.meaning


class Sound(models.Model):
    word = models.ForeignKey(Word,
                             related_name='sounds',
                             on_delete=models.CASCADE)
    region = models.CharField(choices=[
        ("UK", 'United Kingdom'),
        ('US', 'United States'),
    ], verbose_name='region')
    transcription = models.CharField(max_length=255, blank=True)
    link = models.URLField(blank=True)
    sound = models.FileField(upload_to=sound_path, blank=True, null=True)

    def __str__(self):
        return self.region


class Phrase(models.Model):
    word = models.ForeignKey(Word,
                             related_name='phrases',
                             on_delete=models.CASCADE)
    phrase = models.CharField(max_length=255, blank=True)
    translate = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.phrase


class Form(models.Model):
    word = models.ForeignKey(Word,
                             related_name='forms',
                             on_delete=models.CASCADE)
    part_of_speech = models.CharField(choices=[
        ("adjectival", 'adjectival'),
        ('noun', 'noun'),
        ('verb', 'verb'),
    ])
    condition = models.CharField(max_length=255, blank=True)
    value = models.CharField(max_length=255, blank=True)
