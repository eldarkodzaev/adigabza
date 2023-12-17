from urllib.parse import urlencode

import requests
from django.core.paginator import Paginator
from django.views.generic import TemplateView

from adigabza.settings import API_HOST
from .forms import NumeralForm, NumeralRangeForm
from .settings import APP_PATH, PAGINATION_PER_PAGE


class KabNumeralsListView(TemplateView):
    template_name = 'kab_numerals/kab_numerals_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if page := self.request.GET.get('page'):
            response = requests.get(f'{API_HOST}{APP_PATH}?{urlencode(self.request.GET)}&page={page}')
        else:
            response = requests.get(f'{API_HOST}{APP_PATH}?{urlencode(self.request.GET)}&page=1')
        context['numerals'] = response.json()
        context['numeral_form'] = NumeralForm()
        context['numeral_range_form'] = NumeralRangeForm()
        paginator = Paginator(object_list=self.numerals_list, per_page=PAGINATION_PER_PAGE)
        context['paginator'] = paginator
        return context

    @property
    def numerals_list(self):
        get_params = dict(self.request.GET)
        get_params.pop('page', None)
        return requests.get(f'{API_HOST}{APP_PATH}?{urlencode(get_params, doseq=True)}').json()