"""
Модуль выполняет диспетчеризацию и перенаправление запросов
в указанную функцию обработчик
"""
from django.contrib import admin
from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.print_index, name='home'),
    path('home', views.print_index, name='home'),
    path('faqs', views.print_faqs, name='faqs'),
    path('abouts', views.print_about, name='about_project'),
    path('admin', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
