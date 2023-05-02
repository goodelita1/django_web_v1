from django import forms


class NameForm(forms.Form):
    first = forms.IntegerField(label="triangle")
    second = forms.IntegerField(label="triangle")