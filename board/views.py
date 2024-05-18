from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from .models import Post
from .forms import PostForm, PhotoForm # check: PhotoForm

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
    form_class = PostForm
    success_url ='/post/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_url'] = reverse_lazy('login')
        context['signup_url'] = reverse_lazy('signup')
        return context

    def form_valid(self, form):
        """
        Defines the author of the post.
        Prevents user being able to choose other usernames as author.
        """
        form.instance.user = self.request.user
        return super(AddPost, self).form_valid(form)
