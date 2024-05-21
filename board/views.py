from django.shortcuts import render
from django.views import generic
from django.views.generic import (
    CreateView, ListView, DetailView, DeleteView, UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm


# Create your views here.
class Board(ListView):
    """
    Display overview of posts on board Offers & Requests.
    **Context**
    Context object name customized for readability.
    
    ``queryset``
        All published instances of :model:`bord.Post`
    ***Template:***
    :template:`board/board.html`
    """
    queryset = Post.objects.filter(status=1)
    template_name = "board/board.html"
    model = Post
    context_object_name = "board"


class PostDetail(DetailView):
    """
    Display detailed view of posts on Offers & Requests.
    **Context**
    Context object name customized for readability.
    ``post``
        An instance of :model:`board.Post`.
    ``queryset``
        All published instances of :model:`bord.Post`
    ***Template:***
    :template:`board/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    template_name = "board/post_detail.html"
    model = Post
    context_object_name = "post"


class AddPost(LoginRequiredMixin, CreateView):
    """
    Display Add Post view.
    LoginRequiredMixin checks if user is logged in before running CreateView.
    If user is not logged in and attempts to add post, it redirects user to login page.
    CreateView handles form to add a post in the DOM.
    **Context**
    ``post``
        An instance of :model:`board.Post`.
    ***Template:***
    :template:`board/add_post.html`
    """
    template_name = "board/add_post.html"
    model = Post
    form_class = PostForm
    success_url = "/board/"

    def form_valid(self, form):
        """
        Defines the author of the post.
        Prevents user being able to choose other usernames as author.
        Delay saving post to database: check if image was upoloaded,
            else save post_image as None to database.
            Check: Code from walkthrough project codestar, not working properly.
            Check: (AddPost, self) removed from super() according to Python 3.
        """
        form.instance.user = self.request.user
        post = form.save(commit=False)
        if self.request.FILES.get("post_image"):
            post.post_image = self.request.FILES["post_image"]
        else:
            post.post_image = None
        post.save()
        return super().form_valid(form)


class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit user's own content.
    Utilizes Django's authentication system's mixins to secure edit of only own content.
    **Context**
    ``post``
        An instance of :model:`board.Post`.
    ***Template:***
    :template:`board/edit_post.html`
    """
    template_name = "board/edit_post.html"
    model = Post
    form_class = PostForm
    sucess_url = "/board/"

    def test_func(self):
        """
        Required for UserPassesTextMixin.
        Returns True if user passes test: is content author.
        Returns False if user is not content author and throws 403 error.
        """
        return self.request.user == self.get_object().author


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete user's own content.
    Utilizes Django's authentication system's mixins to secure deletion of only own content.
    Template_name field is not required.
    **Context**
    ``post``
        An instance of :model:`board.Post`.
    ***Template:***
    :template:`board/post_confirm_delete.html`
    """
    model = Post
    success_url = "/board/"

    def test_func(self):
        """
        Required for UserPassesTextMixin.
        Returns True if user passes test: is content author.
        Returns False if user is not content author and throws 403 error.
        """
        return self.request.user == self.get_object().author
