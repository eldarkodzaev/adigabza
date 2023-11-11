from django.urls import path
from .views import KabWordDetailView, KabRusDictionaryView, CategoryDetailView

app_name = 'kab_rus_dictionary'

urlpatterns = [
    path('<slug:slug>/', KabWordDetailView.as_view(), name='kab_word_detail'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('', KabRusDictionaryView.as_view(), name='kab_rus_dictionary'),
]
