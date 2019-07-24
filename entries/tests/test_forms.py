from entries import forms
from django.test import TestCase


class TestEntryForm(TestCase):
    def test_entry_form_invalid(self):
        invalid_data = {
            'text': {},
            'confirm': 'not secret'
        }
        form = forms.EntryForm(data=invalid_data)
        assert form.is_valid() is False, 'should be invalid since nothing <=0'
        self.assertTrue(form.errors), 'should return the error message'

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
