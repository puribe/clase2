from django.test import TestCase,Client
from myapp.views import ping

# Test del endpoint ping
class PingTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_endpoint_ping_responde_ping_pong(self):
        response = self.client.get('/ping/')
        self.assertEqual(response.status_code,200)
        self.assertJSONEqual(response.content, {'ping': 'pong'})

    def test_endpoint_ping_responde_404(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)