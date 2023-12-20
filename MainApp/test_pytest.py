import pytest
from hf.py import translator
from hf.py import summarizer

def test_translator():
article_en = "This is a test article in English"
translated = translator(article_en)
assert translated == "Это тестовая статья на русском языке"

def test_summarizer():
article_text = "Это тестовая статья на русском языке. Она содержит некоторый текст для проверки функции summarizer."
summary = summarizer(article_text)
assert summary == "Тестовая статья на русском языке. Проверка функции summarizer."




import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_home_page(client):
   response = client.get(reverse('home'))
   assert response.status_code == 200