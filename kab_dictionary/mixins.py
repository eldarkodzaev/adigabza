import requests

from django.conf import settings
from django.core.paginator import Paginator

from .settings import APP_PATH, PAGINATION_PER_PAGE


class CategoryContextMixin:
    """
    Добавляет в контекст информацию о категориях
    """

    def get_context_data(self, **kwargs):
        context = {}
        response = requests.get(f'{settings.API_HOST}{APP_PATH}categories/')
        response_json = response.json()
        context['response'] = response_json
        context['categories_list'] = response_json['results']
        return context


class PaginatorContextMixin:
    """
    Добавляет в контекст пагинатор
    """

    def get_context_data(self, **kwargs):
        context = {}
        object_list = kwargs.pop('object_list')
        page = kwargs.pop('page')
        paginator = Paginator(object_list=object_list, per_page=PAGINATION_PER_PAGE)
        context['paginator'] = paginator
        page_obj = paginator.get_page(page)
        context['page_obj'] = page_obj
        context['paginator_range'] = paginator.get_elided_page_range(page_obj.number, on_each_side=5)
        return context
