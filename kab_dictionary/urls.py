from django.urls import path
from .views import KabWordDetailView

app_name = 'kab_rus_dictionary'

urlpatterns = [
    path('<slug:slug>/', KabWordDetailView.as_view(), name='kab_word_detail')
]
