from django.utils import timezone
from model_mommy import mommy

from links.models import Link


class TestHelloView:

    url = '/app/'

    def test_page_works(self, db, client):
        r = client.get(self.url)
        assert r.status_code == 200

    def test_random_name_when_name_field_is_empty(self, db, client):
        r = client.post(self.url, data={
            'name': '',
            'destination': 'https://something.invalid',
        })
        assert r.status_code == 200 and Link.objects.get(destination='https://something.invalid').name

    def test_expiration_can_be_empty(self, db, client):
        r = client.post(self.url, data={
            'name': 'test-expiration',
            'destination': 'https://something.invalid',
        })
        assert r.status_code == 200 and Link.objects.get(name='test-expiration').expiration_date is None


class TestRedirectView:

    url = '/app/r/'

    def test_redirect_works(self, db, client):
        mommy.make(Link, name='test', destination='https://something.invalid')
        r = client.get(self.url + 'test/')
        assert r.status_code == 302 and r.url == 'https://something.invalid'

    def test_expiration_works(self, db, client):
        mommy.make(Link, name='test', destination='https://something.invalid',
                   expiration_date=timezone.now() - timezone.timedelta(days=1))
        r = client.get(self.url + 'test/')
        assert r.status_code == 410
