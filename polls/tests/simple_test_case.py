from django.test import SimpleTestCase
from django.urls import reverse

class URLTests(SimpleTestCase):

    # ====================================================================================
    # Test Case 1 ~ Checks that the URL name 'polls:index' correctly resolves to '/polls/'
    # ====================================================================================
    def test_index_url(self):
        url = reverse('polls:index')
        self.assertEqual(url, '/polls/')