from django.core.paginator import InvalidPage, Page
from django.http import Http404
from django.utils.translation import gettext as _
from django.views.generic import ListView

from .forms import NumeralForm, NumeralRangeForm
from .models import KabNaturalNumber
from .paginators import NumeralsPaginator


class KabNumeralsListView(ListView):
    model = KabNaturalNumber
    template_name = 'kab_numerals/kab_numerals_list.html'
    context_object_name = 'numbers'
    paginator_class = NumeralsPaginator
    paginate_by = 100
    paginate_orphans = 10

    def get_queryset(self):
        params = self._get_params()
        return KabNaturalNumber.objects.only(
            'number', 'translate_decimal')[params['from']:params['to'] + 1:params['step']]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        page: Page = context['page_obj']
        context['paginator_range'] = page.paginator.get_elided_page_range(page.number)
        context['numeral_form'] = NumeralForm()
        context['numeral_range_form'] = NumeralRangeForm()
        return context

    def paginate_queryset(self, queryset, page_size):
        try:
            return super().paginate_queryset(queryset, page_size)
        except Http404:
            paginator = self.get_paginator(
                queryset, page_size, orphans=self.get_paginate_orphans(),
                allow_empty_first_page=self.get_allow_empty())
            try:
                page = paginator.page(1)
                return paginator, page, page.object_list, page.has_other_pages()
            except InvalidPage as e:
                raise Http404(_('Invalid page (%(page_number)s): %(message)s') % {
                    'page_number': paginator.page_number,
                    'message': str(e)
                })

    def _get_params(self):
        try:
            start = abs(int(self.request.GET.get('start')))
        except (ValueError, TypeError):
            start = 1

        try:
            end = abs(int(self.request.GET.get('end')))
        except (ValueError, TypeError):
            end = 100

        try:
            step = int(self.request.GET.get('step'))
        except (ValueError, TypeError):
            step = 1

        return {'from': start, 'to': end, 'step': step}
