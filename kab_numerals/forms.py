from django import forms

from kab_numerals.settings import MIN_NUMERAL, MAX_NUMERAL


class NumeralForm(forms.Form):
    number = forms.IntegerField(
        min_value=MIN_NUMERAL,
        max_value=MAX_NUMERAL,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите число",
            }
        )
    )

    translation = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "readonly": True,
                "rows": 1,
            }
        )
    )


class NumeralRangeForm(forms.Form):
    start = forms.IntegerField(
        min_value=MIN_NUMERAL,
        max_value=MAX_NUMERAL,
        initial=1,
        label="От",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите начальное значение",
            }
        )
    )

    end = forms.IntegerField(
        min_value=MIN_NUMERAL,
        max_value=MAX_NUMERAL,
        initial=100,
        label="До",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите конечное значение"
            }
        )
    )

    step = forms.IntegerField(
        min_value=1,
        initial=1,
        label="Шаг",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Введите шаг"
            }
        )
    )
