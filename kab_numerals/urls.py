from django.urls import path
from .views import KabNumeralsListView


urlpatterns = [
    path('', KabNumeralsListView.as_view(), name='numerals'),
]
