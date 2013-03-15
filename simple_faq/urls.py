#! coding: utf-8

from django.conf.urls import patterns, url
from simple_faq.views import Topics

urlpatterns = patterns(
    '',
    url(r'^', Topics.as_view(), name='faq'),
)

__author__ = 'lgomez'
