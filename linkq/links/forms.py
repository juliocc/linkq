from django.forms import ModelForm
from .models import Link

class NextLinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['summary']
