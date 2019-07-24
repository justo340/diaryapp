from django.test import TestCase
from django.utils import timezone
from entries.models import Entry


class TestEntry(TestCase):
    def create_Entry(self, text='jhghgf'):
        return Entry.objects.create(
            text='jhghgf', date_posted=timezone.now())

    def test_Entry_creation(self):
        created = self.create_Entry()
        self.assertTrue(isinstance(created, Entry))
        self.assertTrue(created.__str__(), created.id)
