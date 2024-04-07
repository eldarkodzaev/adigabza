from django.views.generic import TemplateView


class MainPageView(TemplateView):
    """
    Контроллер для отображения главной страницы сайта
    """
    template_name = 'home.html'
