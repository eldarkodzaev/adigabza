import requests
from django.core.paginator import Page
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from adigabza.settings import API_HOST
from .forms import KabWordSearchForm
from .models import KabWord, Translation, Category
from .paginators import DictionaryPaginator


class KabWordDetailView(DetailView):
    model = KabWord
    template_name = 'kab_dictionary/kab_word_detail.html'
    context_object_name = 'word'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(f'{API_HOST}kab-rus-dictionary/{self.object.slug}/')
        content_json = response.json()
        context['content_json'] = content_json
        return context


class KabRusDictionaryView(FormMixin, ListView):
    model = KabWord
    template_name = 'kab_dictionary/main.html'
    form_class = KabWordSearchForm
    context_object_name = 'words'
    paginator_class = DictionaryPaginator
    paginate_by = 10
    paginate_orphans = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(f'{API_HOST}kab-rus-dictionary/')
        content_json = response.json()
        context['content_json'] = content_json['results']
        page: Page = context['page_obj']
        context['paginator_range'] = page.paginator.get_elided_page_range(page.number)
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'kab_dictionary/category_detail_view.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['words'] = Translation.objects.filter(
            categories__slug__contains=self.object.slug).select_related('word')
        return context
