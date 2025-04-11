from django.test import TestCase,Client
from myapp.views import ping
from datetime import datetime
from unittest.mock import patch
# Test del endpoint ping
class PingTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_endpoint_ping_responde_ping_pong(self):
        fecha_esperada = "2024-03-01T12:00:00"  # Fecha esperada en formato ISO
        with patch('myapp.views.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime.fromisoformat(fecha_esperada)
            response = self.client.get('/ping/')
            self.assertEqual(response.status_code, 200)
            self.assertJSONEqual(response.content, {'ping': 'pong', 'date': fecha_esperada})
 

    def test_endpoint_ping_responde_404(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)