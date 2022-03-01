from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTest(TestCase):
    def test_example(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')
        posts = response.context['posts']
