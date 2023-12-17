"""
Модуль содержит классы моделей реализованных в приложении форм.
"""
from django.db import models
# Create your models here.
class Translate(models.Model):
    '''
    Модель формы Translate
    '''
    article = models.TextField()

class Summary(models.Model):
    '''
       Модель формы Summary
    '''
    translate_text = models.TextField()

