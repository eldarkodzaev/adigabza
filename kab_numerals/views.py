from urllib.parse import urlencode

import requests
from django.core.paginator import Paginator
from django.views.generic import TemplateView

from adigabza.settings.base import API_HOST
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
        context['numeral_range_form'] = NumeralRangeForm(
            initial=self.__get_initial_data_for_numeral_range_form()
        )
        paginator = Paginator(object_list=self.numerals_list, per_page=PAGINATION_PER_PAGE)
        context['paginator'] = paginator
        page_obj = paginator.get_page(page)
        context['page_obj'] = page_obj
        context['paginator_range'] = paginator.get_elided_page_range(page_obj.number, on_each_side=5)
        return context

    @property
    def numerals_list(self):
        get_params = dict(self.request.GET)
        get_params.pop('page', None)
        return requests.get(f'{API_HOST}{APP_PATH}?{urlencode(get_params, doseq=True)}').json()

    def get_params(self) -> dict:
        params = dict(self.request.GET)
        start = params.pop('start', None)
        end = params.pop('end', None)
        return {'start': start, 'end': end}
    
    def __get_initial_data_for_numeral_range_form(self) -> dict:
        return {
            'start': self.request.GET.get('start', 1),
            'end': self.request.GET.get('end', 100),
            'step': self.request.GET.get('step', 1),
        }
