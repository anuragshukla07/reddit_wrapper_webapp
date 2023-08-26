from django.test import TestCase
from django.urls import reverse

class GetArticlesViewTestCase(TestCase):    #basic test to check whether the page is being displayed or not
    def test_articles_view(self):
        response = self.client.get(reverse('articles'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Reddit Articles</title>')
