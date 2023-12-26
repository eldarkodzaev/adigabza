from django import forms

from kab_numerals.settings import MIN_NUMERAL, MAX_NUMERAL


class NumeralForm(forms.Form):
    number = forms.IntegerField(min_value=MIN_NUMERAL, max_value=MAX_NUMERAL)


class NumeralRangeForm(forms.Form):
    start = forms.IntegerField(min_value=MIN_NUMERAL, max_value=MAX_NUMERAL, initial=1)
    end = forms.IntegerField(min_value=MIN_NUMERAL, max_value=MAX_NUMERAL, initial=100)
    step = forms.IntegerField(min_value=1, initial=1)
