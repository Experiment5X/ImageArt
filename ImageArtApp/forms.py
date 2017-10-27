from django import forms


class ArtFunctionForm(forms.Form):
    red_func = forms.CharField(label='Red')
    green_func = forms.CharField(label='Green')
    blue_func = forms.CharField(label='Blue')
