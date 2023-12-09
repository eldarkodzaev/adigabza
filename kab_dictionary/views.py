from django.views.generic import TemplateView
from django.views.generic.edit import FormMixin


class KabWordDetailView(TemplateView):
    pass


class KabRusDictionaryView(FormMixin, TemplateView):
    pass


class CategoryDetailView(TemplateView):
    pass
