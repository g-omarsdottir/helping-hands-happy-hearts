from django.views import generic
from django.shortcuts import render


# Create your views here.
class Index(generic.TemplateView):
    """
    Should be ListView, but that throws an error.
    Reevaluate after creating Models.
    """

    template_name = "home/index.html"
