from django.core.paginator import Page
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from .models import KabWord, Translation, Category
from .forms import KabWordSearchForm
from kab_numerals.paginators import NumeralsPaginator


class KabWordDetailView(DetailView):
    model = KabWord
    template_name = 'kab_dictionary/kab_word_detail.html'
    context_object_name = 'word'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['translations_list'] = self.object.translations.select_related(
            'source', 'word__borrowed_from', 'part_of_speech')
        return context


class KabRusDictionaryView(FormMixin, ListView):
    model = KabWord
    template_name = 'kab_dictionary/main.html'
    form_class = KabWordSearchForm
    context_object_name = 'words'
    paginator_class = NumeralsPaginator
    paginate_by = 10
    paginate_orphans = 3

    def get_queryset(self):
        word_param = self.request.GET.get('word')
        if word_param:
            return Translation.objects.select_related('word').filter(word__word__icontains=word_param)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page: Page = context['page_obj']
        context['paginator_range'] = page.paginator.get_elided_page_range(page.number)
        context['full_path'] = self.request.get_full_path()
        if self.object_list:
            context['translations_count'] = self.object_list.all().count()
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'kab_dictionary/category_detail_view.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['words'] = Translation.objects.filter(categories__slug__contains=self.object.slug).select_related('word')
        return context
