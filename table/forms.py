from django import forms

HEIGHT_CHOICES = (
    ('', ''),
    ('height__gt', '>'),
    ('height__lt', '<'),
    ('height__gte', '>='),
    ('height__lte', '<=')
)

SPEED_CHOICES = (
    ('', ''),
    ('speed__gt', '>'),
    ('speed__lt', '<'),
    ('speed__gte', '>='),
    ('speed__lte', '<=')
)

ORDER_BY_CHOICES = (
    ('', ''),
    ('asc', 'По возрастанию'),
    ('desc', 'По убыванию'),
)


class GPSDataForm(forms.Form):
    height = forms.CharField(
        label='Высота',
        required=False,
        widget=forms.NumberInput(),
    )
    height_condition = forms.ChoiceField(
        label='Условие для высоты',
        choices=HEIGHT_CHOICES,
        required=False,
    )

    speed = forms.CharField(
        label='Скорость',
        required=False,
    )
    speed_condition = forms.ChoiceField(
        label='Условие для скорости',
        choices=SPEED_CHOICES,
        required=False,
    )

    height__order_by = forms.ChoiceField(
        label='Упорядочить высоту',
        choices=ORDER_BY_CHOICES,
        required=False,
    )
    speed__order_by = forms.ChoiceField(
        label='Упорядочить скорость',
        choices=ORDER_BY_CHOICES,
        required=False,
    )
