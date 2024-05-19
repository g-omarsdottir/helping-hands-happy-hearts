from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm, PhotoForm # check: PhotoForm

# Create your views here.
class Board(ListView):
    """
    Display content Offers & Requests
    Context object name customized for readability.
    ***Template:***
    :template:`board/board.html`

    """
    template_name = 'board/board.html'
    model = Post
    context_object_name = 'board'


class AddPost(LoginRequiredMixin, CreateView):
    """
    Display Add Post view.
    LoginRequiredMixin checks if user is logged in before running CreateView.
    If user is not logged in and attempts to add post, it redirects user to login page.
    CreateView handles form to add a post in the DOM.
    ***Template:***
    :template:`board/add_post.html`
    """
    template_name = 'board/add_post.html'
    model = Post
    form_class = PostForm
    success_url ='/post/'

    def form_valid(self, form):
        """
        Defines the author of the post.
        Prevents user being able to choose other usernames as author.
        """
        form.instance.user = self.request.user
        return super(AddPost, self).form_valid(form)
