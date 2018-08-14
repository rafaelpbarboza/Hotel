# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class renderIndex(TemplateView):
    template_name = 'index.html'

