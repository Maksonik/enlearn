from django.contrib import admin
from django import forms
from .models import Word, Description, Sound, Phrase, Form, Example



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

class ExamplesInline(admin.TabularInline):
    model = Example.words.through


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'rank')
    inlines = [DescriptionInline, SoundInline, FormInline, PhraseInline, ExamplesInline]


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


class ExampleAdminForm(forms.ModelForm):
    class Meta:
        model = Example
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ограничиваем выбор слов только теми, которые уже привязаны к текущему примеру
        self.fields['words'].queryset = Word.objects.all()[:50]


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ('example', 'translate')
    filter_horizontal = ('words',)
    form = ExampleAdminForm
