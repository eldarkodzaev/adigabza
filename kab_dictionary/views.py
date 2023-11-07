from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from .models import KabWord
from .forms import KabWordSearchForm


class KabWordDetailView(DetailView):
    model = KabWord
    template_name = 'kab_dictionary/kab_word_detail.html'
    context_object_name = 'word'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['translations_list'] = self.object.translations.all()
        return context


class KabRusDictionaryView(FormMixin, ListView):
    model = KabWord
    template_name = 'kab_dictionary/main.html'
    form_class = KabWordSearchForm
    context_object_name = 'words'

    def get_queryset(self):
        word_param = self.request.GET.get('word')
        if word_param:
            return KabWord.objects.only('id', 'word', 'slug').filter(word__icontains=word_param)
