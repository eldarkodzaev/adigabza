import requests

from django.conf import settings
from django.http import Http404
from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin

from .forms import KabWordSearchForm
from .mixins import CategoryContextMixin, PaginatorContextMixin
from .settings import APP_PATH


class KabWordDetailView(TemplateView):
    """
    Отображает детальную страницу кабардино-черкесского слова
    """

    template_name = 'kab_dictionary/kab_word_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(f'{settings.API_HOST}{APP_PATH}{context["slug"]}/', timeout=3.05)
        if response.status_code == 404:
            raise Http404
        context['word'] = response.json()
        return context


class KabRusDictionaryView(CategoryContextMixin, PaginatorContextMixin, FormMixin, TemplateView):
    """
    Отображает страницу кабардино-черкесско-русского словаря
    """

    form_class = KabWordSearchForm
    template_name = 'kab_dictionary/main.html'
    __words = requests.get(f'{settings.API_HOST}{APP_PATH}all', timeout=3.05).json()

    def get_context_data(self, **kwargs):
        category_context = super().get_context_data(**kwargs)
        form_context = super(PaginatorContextMixin, self).get_context_data(**kwargs)
        context = form_context | category_context
        if word := self.request.GET.get('word'):
            response = requests.get(f'{settings.API_HOST}{APP_PATH}?word={word}', timeout=3.05)
            context['words'] = response.json()
            context['form'] = self.form_class(initial={'word': word})
        else:
            if page := self.request.GET.get('page'):
                response = requests.get(f'{settings.API_HOST}{APP_PATH}?page={page}', timeout=3.05)
                context['words'] = response.json()['results']
            else:
                context['words'] = requests.get(f'{settings.API_HOST}{APP_PATH}?page=1', timeout=3.05).json()['results']
                page = '1'
            paginator_context = super(CategoryContextMixin, self).get_context_data(object_list=self.__words, page=page)
            context |= paginator_context
        return context


class CategoryView(TemplateView):
    """
    Отображает одну категорию и слова, относящиеся к ней
    """

    template_name = 'kab_dictionary/category_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(f'{settings.API_HOST}{APP_PATH}categories/{context["slug"]}/', timeout=3.05)
        if response.status_code == 404:
            raise Http404
        response_json = response.json()
        context['response'] = response_json
        context['category'] = response_json['category']
        context['translations'] = response_json['translations']
        return context


class CategoriesView(TemplateView):
    """
    Отображает список категорий
    """

    template_name = 'kab_dictionary/categories_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(f'{settings.API_HOST}{APP_PATH}categories/', timeout=3.05)
        response_json = response.json()
        context['response'] = response_json
        context['categories_list'] = response_json['results']
        return context
