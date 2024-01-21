from django.urls import path
from .views import KabWordDetailView, KabRusDictionaryView, CategoryView, CategoriesView

app_name = 'kab_rus_dictionary'

urlpatterns = [
    path('categories/<slug:slug>/', CategoryView.as_view(), name='category_detail'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('<slug:slug>/', KabWordDetailView.as_view(), name='kab_word_detail'),
    path('', KabRusDictionaryView.as_view(), name='kab_rus_dictionary'),
]
