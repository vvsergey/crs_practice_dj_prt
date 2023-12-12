from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def print_index(request) -> HttpResponse:
    return render(request,'index.html')


def print_faqs(request) -> HttpResponse:
    return render(request, 'faqs.html')


def print_about(request) -> HttpResponse:
    return render(request, 'about.html')
