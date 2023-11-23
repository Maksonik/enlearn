from django.contrib import admin
from word.models import Word


# Register your models here.


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['title',
                    'description',
                    'sound']
