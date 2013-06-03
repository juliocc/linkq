from django import forms
from django.core.validators import URLValidator
from werkzeug.urls import url_fix
from tinymce.widgets import TinyMCE

from .models import Link

class NextLinkForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(NextLinkForm, self).__init__(*args, **kwargs)
        self.fields['summary'].required = True

    class Meta:
        model = Link
        fields = ['summary']


class MultiURLField(forms.Field):
    def to_python(self, value):
        "Normalize data to a list of strings."

        # Return an empty list if no input was given.
        if not value:
            return []
        return [url_fix(x.strip()) for x in value.split("\n") if x.strip()]

    def validate(self, value):
        "Check if value consists only of valid emails."

        # Use the parent's handling of required fields, etc.
        super(MultiURLField, self).validate(value)

        urlvalidator = URLValidator()
        for url in value:
            urlvalidator(url)

class AddLinkForm(forms.Form):
    urls = MultiURLField(widget=forms.Textarea)

#    def validate(self):
        
