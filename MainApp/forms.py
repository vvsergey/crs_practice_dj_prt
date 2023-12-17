'''
Модуль с описанием форм в виде классов
'''
from django.forms import ModelForm, TextInput, Textarea
from MainApp.models import Translate, Summary

class TranslateFrom(ModelForm):
    '''
    Класс для генерации формы Translate
    '''
    class Meta:
        model = Translate
        fields = ['article']
        widgets = {
            'article': Textarea(attrs={
                'placeholder': 'Вставьте сюда статью на английском, которую нужно перевести',
                'class': 'form-control',
            })
        }
        labels = {
            'article':'123'
        }


class SummaryForm(ModelForm):
    '''Класс для генерации формы Summary'''
    class Meta:
        model = Summary
        fields = ['translate_text']
        widgets = {
            'translate_text': Textarea(attrs={
                'placeholder': 'Вставьте сюда статью по которой хотите получить краткое содержание',
                'class': 'form-control',
            })
        }
        labels = {
            'translate_text':''
        }