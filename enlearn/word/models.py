import requests
from django.core.files.base import ContentFile
from django.db import models
from django.urls import reverse

PART_OF_SPEECH = [
    ("adjectival", 'adjectival'),
    ('noun', 'noun'),
    ('verb', 'verb'),
    ('alliance', 'alliance'),
    ('adverb', 'adverb'),
    ('pronoun', 'pronoun'),
    ('other', 'other'),
    ('pretext', 'pretext'),
    ('interjection', 'interjection'),
]


def sound_path(instance, filename):
    return f'sounds/{instance.word}/{instance.region}/{filename}'


class Word(models.Model):
    name = models.CharField(max_length=255, unique=True)
    short_description = models.CharField(max_length=1000, blank=True, null=True)
    rank = models.CharField(default='> 22000', blank=True, null=True)

    class Meta:
        ordering = ['name', 'rank']

    def __str__(self):
        return self.name





class Example(models.Model):
    example = models.CharField(max_length=500, unique=True)
    translate = models.CharField(max_length=500)
    words = models.ManyToManyField(Word,
                                   related_name='examples',
                                   blank=True)

    def __str__(self):
        return self.example


class Description(models.Model):
    word = models.ForeignKey(Word,
                             related_name='descriptions',
                             on_delete=models.CASCADE)
    part_of_speech = models.CharField(choices=PART_OF_SPEECH)
    general_meaning = models.CharField(max_length=255, blank=True, null=True)
    deep_meaning = models.CharField(max_length=255, blank=True, null=True)
    translate = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.general_meaning


class Sound(models.Model):
    word = models.ForeignKey(Word,
                             related_name='sounds',
                             on_delete=models.CASCADE)
    region = models.CharField(choices=[
        ("UK", 'United Kingdom'),
        ('US', 'United States'),
    ], verbose_name='region')
    transcription = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    sound = models.FileField(upload_to=sound_path, blank=True, null=True)

    def __str__(self):
        return self.region

    def save(self, *args, **kwargs):
        if self.link and not self.sound:
            try:
                r = requests.get(sepklf.link)
                self.sound.save(self.link.split("/")[-1], ContentFile(r.content), save=False)
            except Exception as e:
                print('Ошибка', e)
        super().save(*args, **kwargs)


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
    part_of_speech = models.CharField(choices=PART_OF_SPEECH)
    condition = models.CharField(max_length=255, blank=True)
    value = models.CharField(max_length=255, blank=True)
