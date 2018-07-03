class TestHelloView:

    url = '/app/'

    def test_page_works(self, client):
        r = client.get(self.url)
        assert r.status_code == 200
