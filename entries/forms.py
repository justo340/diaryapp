from django import forms
from django.forms import ModelForm
from .models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('text', )

    def clean_text(self):
        cleaned_words = self.cleaned_data.get('text')
        if len(cleaned_words) <= 0:
            raise forms.ValidationError({
                'confirm': 'please enter some more words'})
        return cleaned_words

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update(
            {'class': 'textarea', 'placeholder': "what's on your mind?"})
        '''this is used to update the textarea from the  default one,
        the widget just refers to the textarea region
        in the add.html template'''
