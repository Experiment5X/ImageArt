from django import forms


class ArtFunctionForm(forms.Form):
    red_func = forms.CharField(label='Red', initial='x')
    green_func = forms.CharField(label='Green', initial='x * y / 175')
    blue_func = forms.CharField(label='Blue', initial='127')
