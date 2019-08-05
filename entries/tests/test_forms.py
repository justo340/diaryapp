from entries import forms
from django.test import TestCase
# from entries.models import Entry
# from django.core.alidation import ValidationError


class TestEntryForm(TestCase):
    def test_entry_form_invalid(self):
        invalid_data = {
            'text': {},
            'confirm': 'not secret'
        }
        form = forms.EntryForm(data=invalid_data)
        # try:
        #     c.full_clean()
        # except ValidationError as e:
        #     self.assertTrue('cleaned_words' in e.message_dict)
        assert form.is_valid() is False, 'should be invalid since nothing <=0'
        # assert form.errors() is True, 'should return the error message'

    def test_entry_form_valid(self):
        valid_data = {
            'text': {'hey boy'},
            'confirm': 'secret'
        }
        form = forms.EntryForm(data=valid_data)
        cleaned_words = {'text': 'hey boy'}
        form = forms.EntryForm(data=cleaned_words)
        assert form.is_valid() is True, 'should be valid if the data match'
        self.assertFalse(form.errors), 'should not return the error message'
