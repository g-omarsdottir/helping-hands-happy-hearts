from django.shortcuts import render
from django.views import generic

# Create your views here.
class BoardView(generic.TemplateView):
    """
    Display content Offers & Requests
    Might be ListView (check: home/views)
    ***Template:***
    :template:`board/board.html`

    """
    template_name = 'board/board.html'
