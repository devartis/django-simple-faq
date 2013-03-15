#! coding: utf-8
from django.contrib import admin
from simple_faq.models import Topic, Question

admin.site.register(Topic)
admin.site.register(Question)

__author__ = 'lgomez'
