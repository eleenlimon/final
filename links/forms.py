from django import forms

from .models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['name', 'url', 'slug']

# django has a builtin form----(Modelform)--import model Link to specify what fields want to use/implement
