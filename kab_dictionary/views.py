from django.shortcuts import render
from django.views.generic import DetailView

from kab_dictionary.models import KabWord


class KabWordDetailView(DetailView):
    model = KabWord
    template_name = 'kab_dictionary/kab_word_detail.html'
    context_object_name = 'word'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['translations_list'] = self.object.translations.all()
        return context
