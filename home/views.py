from django.views import generic
from django.shortcuts import render

# Create your views here.
class Index(generic.TemplateView):
    template_name = 'home/index.html'
