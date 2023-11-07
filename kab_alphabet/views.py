from django.shortcuts import render
from django.views.generic import ListView, DetailView

from kab_alphabet.models import KabLetter
from kab_dictionary.models import KabWord


class AlphabetListView(ListView):
    model = KabLetter
    template_name = 'kab_alphabet/kab_alphabet_list.html'
    context_object_name = 'alphabet'


class LetterDetailView(DetailView):
    model = KabLetter
    template_name = 'kab_alphabet/kab_letter_detail.html'
    context_object_name = 'letter'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['words_count'] = KabWord.objects.filter(letter=self.object).count()
        context['words'] = KabWord.objects.filter(letter=self.object)
        return context
