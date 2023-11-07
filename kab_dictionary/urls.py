from django.urls import path
from .views import KabWordDetailView, KabRusDictionaryView

app_name = 'kab_rus_dictionary'

urlpatterns = [
    path('<slug:slug>/', KabWordDetailView.as_view(), name='kab_word_detail'),
    path('', KabRusDictionaryView.as_view(), name='kab_rus_dictionary'),
]
