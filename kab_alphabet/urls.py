from django.urls import path

from kab_alphabet.views import AlphabetListView, LetterDetailView

app_name = 'kab_alphabet'

urlpatterns = [
    path('', AlphabetListView.as_view(), name='alphabet'),
    path('<slug>/', LetterDetailView.as_view(), name='letter'),
]
