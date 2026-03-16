from django.test import LiveServerTestCase
import requests

class PollsLiveServerTests(LiveServerTestCase):

    # ==========================================
    # Test Case 1 ~ Check Polls Index Page
    # ==========================================
    def test_polls_index_page_loads(self):
        response = requests.get(self.live_server_url + '/polls/')
        self.assertEqual(response.status_code, 200)