from model_mommy import mommy

from links.models import Link


class TestHelloView:

    url = '/app/'

    def test_page_works(self, db, client):
        r = client.get(self.url)
        assert r.status_code == 200


class TestRedirectView:

    url = '/app/r/'

    def test_redirect_works(self, db, client):
        mommy.make(Link, name='test', destination='https://something.invalid')
        r = client.get(self.url + 'test/')
        assert r.status_code == 302 and r.url == 'https://something.invalid'
