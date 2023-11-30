from django.contrib import admin
from .models import Word, Description, Sound, Phrase, Form, Learner


@admin.register(Learner)
class LearnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'word', 'stage_learning_word', 'created', 'updated']


class DescriptionInline(admin.TabularInline):
    model = Description
    ordering = ['part_of_speech']

class SoundInline(admin.TabularInline):
    model = Sound
    extra = 2

class FormInline(admin.TabularInline):
    model = Form

class PhraseInline(admin.TabularInline):
    model = Phrase

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'rank')
    inlines = [ DescriptionInline,SoundInline, FormInline, PhraseInline]

@admin.register(Description)
class WordDescriptionAdmin(admin.ModelAdmin):
    pass

@admin.register(Sound)
class SoundAdmin(admin.ModelAdmin):
    pass

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    pass

@admin.register(Phrase)
class PhraseAdmin(admin.ModelAdmin):
    pass
