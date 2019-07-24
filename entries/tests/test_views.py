from django.urls import reverse
from entries import views
from entries.views import EntryListView
from django.test import RequestFactory, TestCase
from entries.forms import EntryForm


class TestEntryListViews(TestCase):
    def test_EntryListView(self):
        req = RequestFactory().get('')
        respo = EntryListView.as_view()(req)
        assert respo.status_code == 200, 'called by anyone'


class TestAdd(TestCase):
    url = RequestFactory().get('add/')
    response = views.add(url)
    form = EntryForm(data={'text': 'text'})
    assert form.is_valid() is True
    assert response.status_code == 200

    def test_add_post(self):
        url = reverse('add')
        response = self.client.post(url, data={'text': 'this boy'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, '/', status_code=302,
            target_status_code=200, fetch_redirect_response=True)
