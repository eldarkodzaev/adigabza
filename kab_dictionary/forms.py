from django import forms


class KabWordSearchForm(forms.Form):
    word = forms.CharField(max_length=50, label='search',
                           widget=forms.TextInput(attrs={'placeholder': 'Введите слово'}))
