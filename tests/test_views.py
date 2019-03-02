import pytest
from django.core.management import call_command


class TestHelloView:

    url = '/app/'

    def test_page_works(self, client):
        r = client.get(self.url)
        assert r.status_code == 200

    @pytest.mark.django_db
    def test_redirect_work(self, client):
        r = client.get('/app/r/test')
        assert r.status_code == 302

    @pytest.fixture(scope='session')
    def django_db_setup(django_db_setup, django_db_blocker):
        with django_db_blocker.unblock():
            call_command('loaddata', 'links.json')
