from django.contrib import admin
from .models import KabWord, Translation, Category, PartOfSpeech, Source


@admin.register(KabWord)
class KabWordAdmin(admin.ModelAdmin):
    list_display = ['word', 'slug', 'letter', 'same_word', 'category', 'part_of_speech', 'loan_word', 'source']
    list_filter = ['letter', 'category', 'part_of_speech']
    search_fields = ['word']


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ['word', 'translation', 'description']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(PartOfSpeech)
class PartOfSpeechAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'year', 'url']
