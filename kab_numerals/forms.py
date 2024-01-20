from django import forms

from kab_numerals.settings import MIN_NUMERAL, MAX_NUMERAL


def on_key_press_js_code(length: int) -> str:
    return f"if(this.value.length=={length}) return false;"


class NumeralForm(forms.Form):
    number = forms.IntegerField(
        min_value=MIN_NUMERAL,
        max_value=MAX_NUMERAL,
        label="",
        widget=forms.NumberInput(
            attrs={
                "min": MIN_NUMERAL,
                "max": MAX_NUMERAL,
                "placeholder": "Введите число",
                "onKeyPress": on_key_press_js_code(length=9),
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
        widget=forms.NumberInput(
            attrs={
                "min": MIN_NUMERAL,
                "max": MAX_NUMERAL,
                "placeholder": "Введите начальное значение",
                "onKeyPress": on_key_press_js_code(length=6),
            }
        )
    )

    end = forms.IntegerField(
        min_value=MIN_NUMERAL,
        max_value=MAX_NUMERAL,
        initial=100,
        label="До",
        widget=forms.NumberInput(
            attrs={
                "min": MIN_NUMERAL,
                "max": MAX_NUMERAL,
                "placeholder": "Введите конечное значение",
                "onKeyPress": on_key_press_js_code(length=6),
            }
        )
    )

    step = forms.IntegerField(
        min_value=1,
        initial=1,
        label="Шаг",
        widget=forms.NumberInput(
            attrs={
                "min": MIN_NUMERAL,
                "max": MAX_NUMERAL,
                "placeholder": "Введите шаг",
                "onKeyPress": on_key_press_js_code(length=6),
            }
        )
    )
