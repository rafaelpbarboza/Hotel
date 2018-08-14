# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import  PermissionRequiredMixin

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class Dashboard(TemplateView,PermissionRequiredMixin):
    template_name = "Admin/Dashboard.html"
    permission_required = 'user.Active'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Dashboard, self).dispatch(*args, **kwargs)

