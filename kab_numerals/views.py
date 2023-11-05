from django.views.generic import ListView

from .forms import NumeralForm, NumeralRangeForm
from .models import KabNaturalNumber


class KabNumeralsListView(ListView):
    model = KabNaturalNumber
    template_name = 'kab_numerals/kab_numerals_list.html'
    context_object_name = 'numbers'

    def get_queryset(self):
        params = self._get_params()
        return KabNaturalNumber.objects.only(
            'number', 'translate_decimal')[params['from_']:params['to'] + 1:params['step']]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['numeral_form'] = NumeralForm()
        context['numeral_range_form'] = NumeralRangeForm()
        return context

    def _get_params(self):
        try:
            from_ = abs(int(self.request.GET.get('from_')))
        except (ValueError, TypeError):
            from_ = 1

        try:
            to = abs(int(self.request.GET.get('to')))
        except (ValueError, TypeError):
            to = 100

        try:
            step = int(self.request.GET.get('step'))
        except (ValueError, TypeError):
            step = 1

        return {'from_': from_, 'to': to, 'step': step}
