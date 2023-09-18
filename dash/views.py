from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class Dashboard(TemplateView):
    template_name = "dash/dash1.html"


