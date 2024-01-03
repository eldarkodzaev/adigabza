import requests
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin

from adigabza.settings import API_HOST
from .forms import KabWordSearchForm
from .settings import APP_PATH, PAGINATION_PER_PAGE


class KabWordDetailView(TemplateView):
    """
    Отображает детальную страницу кабардино-черкесского слова
    """
    template_name = 'kab_dictionary/kab_word_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(f'{API_HOST}{APP_PATH}{context["slug"]}/')
        context['word'] = response.json()
        return context


class KabRusDictionaryView(FormMixin, TemplateView):
    """
    Отображает страницу кабардино-черкесско-русского словаря
    """
    form_class = KabWordSearchForm
    template_name = 'kab_dictionary/main.html'
    __words = requests.get(f'{API_HOST}{APP_PATH}').json()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if word := self.request.GET.get('word'):
            response = requests.get(f'{API_HOST}{APP_PATH}?word={word}')
            context['words'] = response.json()
        else:
            if page := self.request.GET.get('page'):
                response = requests.get(f'{API_HOST}{APP_PATH}?page={page}')
                context['words'] = response.json()['results']
            else:
                context['words'] = requests.get(f'{API_HOST}{APP_PATH}?page=1').json()['results']
            paginator = Paginator(object_list=self.__words, per_page=PAGINATION_PER_PAGE)
            context['paginator'] = paginator
            page_obj = paginator.get_page(page)
            context['page_obj'] = page_obj
            context['paginator_range'] = paginator.get_elided_page_range(page_obj.number, on_each_side=5)
        response = requests.get(f'{API_HOST}{APP_PATH}categories/')
        response_json = response.json()
        context['response'] = response_json
        context['categories_list'] = response_json['results']
        return context


class CategoryView(TemplateView):
    """
    Отображает одну категорию и слова, относящиеся к ней
    """
    template_name = 'kab_dictionary/category_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(f'{API_HOST}{APP_PATH}category/{context["slug"]}/')
        response_json = response.json()
        context['response'] = response_json
        context['words'] = response_json['results']
        return context


class CategoriesView(TemplateView):
    """
    Отображает список категорий
    """
    template_name = 'kab_dictionary/categories_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(f'{API_HOST}{APP_PATH}categories/')
        response_json = response.json()
        context['response'] = response_json
        context['categories_list'] = response_json['results']
        return context
