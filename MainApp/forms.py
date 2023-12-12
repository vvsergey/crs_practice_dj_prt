from django.forms import ModelForm, TextInput, Textarea
from MainApp.models import Translate, Summary

class TranslateFrom(ModelForm):
    class Meta:
        model = Translate
        fields = ['article']
        widgets = {
            'article': Textarea(attrs={'placeholder': 'Вставьте сюда статью на английском, которую нужно перевести'})
        }
        labels = {
            'article':''
        }


class SummaryForm(ModelForm):
    class Meta:
        model = Summary
        fields = ['translate_text']
        widgets = {
            'translate_text': Textarea(attrs={'placeholder': 'Вставьте сюда статью по которой хотите получить краткое содержание'})
        }
        labels = {
            'translate_text':''
        }