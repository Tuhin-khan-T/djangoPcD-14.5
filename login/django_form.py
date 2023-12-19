from django import forms
from django.forms.widgets import NumberInput

class djangoLoginForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label = "User Email")
    check = forms.BooleanField()
    # file = forms.FileField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982','1983','1984','1985']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()

    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)

    comment = forms.CharField(widget=forms.Textarea)

