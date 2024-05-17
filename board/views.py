from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView
from .models import Post

# Create your views here.
class BoardView(generic.TemplateView):
    """
    Display content Offers & Requests
    Might be ListView (check: home/views)
    ***Template:***
    :template:`board/board.html`

    """
    template_name = 'board/board.html'


class AddPost(CreateView):
    """
    Add Post view.
    ***Template:***
    :template:`board/add_post.html`
    """
    template_name = 'board/add_post.html'
    model = Post
    success_url ='/post/'

    def form_valid(self, form):
        """
        Defines the username posting the post
        Prevents user being able to choose other usernames as author
        """
        def form_valid(self, form):
            form.instance.user = self.request.user
            return super(AddPost, self).form_valid(form)