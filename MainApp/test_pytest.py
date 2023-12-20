import pytest
from django.test import TestCase
from ApplicationAi/hf.py import translator, summarizer

class Def_test(TestCase):
   def test_translator(self):
      article_en = "This is a test article in English"
      translated = translator(article_en)
      self.assertEqual(translated, "Это тестовая статья на английском языке")

   def test_summarizer(self):
      article_text = "Это тестовая статья на русском языке. Она содержит некоторый текст для проверки функции summarizer."
      summary = summarizer(article_text)
      self.assertEqual(summary, "Тестовая статья на русском языке. Проверка функции summarizer.")




from django.urls import reverse

@pytest.mark.django_db
def test_home_page(client):
   response = client.get(reverse('home'))
   assert response.status_code == 200
