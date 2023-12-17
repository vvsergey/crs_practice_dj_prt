from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from MainApp.models import Translate, Summary
from MainApp.forms import TranslateFrom, SummaryForm
from ApplicationAi import hf

"""Модуль содержит функции обработки HTTP запросв и отрисовку представлений."""
# Create your views here.


def print_index(request) -> HttpResponse:
    '''
    Выполянет отрисовку страницы index.html (Главная) и
    отвечает за обработку событий формы
    :param request: объект класса HttpRequest
    :return: Объект класса HttpResponse
    '''
    articles = list()
    translates = Translate.objects.all()
    for translate in translates:
        articles.append(translate.article)

    translate_texts = list()
    summarys = Summary.objects.all()
    for summary in summarys:
        translate_texts.append(summary.translate_text)

    article = request.POST.get('article')
    translate_text = request.POST.get('translate_text')

    if (request.method == 'POST'):
        if (article):
            print(request.POST)
            translateFrom = TranslateFrom(request.POST)
            translateFrom.save()
        if (translate_text):
            summaryForm = SummaryForm(request.POST)
            summaryForm.save()
    
    if (article):
        translate_text = hf.translator(article)

    if (translate_text):
        summ = hf.summarizer(translate_text)
    else:
        summ = ''

    if (not article and len(articles)):
        article = articles[-1]

    if (not translate_text and len(translate_texts)):
        translate_text = translate_texts[-1]

    translateFrom = TranslateFrom({'article': article})
    summaryForm = SummaryForm({'translate_text': translate_text})

    return render(request, 'index.html', {'translateFrom': translateFrom, 'summaryForm': summaryForm, 'summ': summ})


def print_faqs(request) -> HttpResponse:
    '''
    Отрисовывает страницу FAQS
    :param request: объект класса HttpRequest
    :return: Объект класса HttpResponse
    '''
    return render(request, 'faqs.html')


def print_about(request) -> HttpResponse:
    '''
    Отрисовывает страниу About
    :param request: объект класса HttpRequest
    :return: объект класса HttpResponse
    '''

    return render(request, 'about.html')
