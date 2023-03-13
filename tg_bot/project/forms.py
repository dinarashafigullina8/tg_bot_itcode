from django import forms
from project.models import Request


class AddRequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'