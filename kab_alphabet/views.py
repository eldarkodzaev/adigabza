import requests
from django.views.generic import TemplateView

from adigabza.settings import API_HOST
from .settings import APP_PATH


class AlphabetListView(TemplateView):
    template_name = 'kab_alphabet/kab_alphabet_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(f'{API_HOST}{APP_PATH}')
        context['alphabet'] = response.json()
        return context


# class LetterDetailView(TemplateView):
#     template_name = 'kab_alphabet/kab_letter_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['words_count'] = KabWord.objects.filter(letter=self.object).count()
#         context['words'] = KabWord.objects.filter(letter=self.object)
#         return context
