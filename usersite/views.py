from django.shortcuts import render,redirect
from django.views.generic import TemplateView, RedirectView
from django.views.generic.edit import DeleteView
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import *
# from .forms import *


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context