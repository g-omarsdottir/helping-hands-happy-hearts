from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


# Create your views here.
class Board(ListView):
    """
    Display overview of posts on board Offers & Requests
    Related to :model:`board.Post`
    **Context**
    Context object name customized for readability
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
    Display detailed view of posts on Offers & Requests
    Related to :model:`board.Post`
    **Context**
    Context object name customized for readability.
    ``post``
        An instance of :model:`board.Post`
    ``queryset``
        All published instances of :model:`bord.Post`
    ``likes``
        An instance of :model:`board.Post`
    ``total_likes``
        An instance of :model:`board.Post`
    ***Template:***
    :template:`board/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    template_name = "board/post_detail.html"
    model = Post
    context_object_name = "post"

    def get_object(self):
        """
        Specify to return both slug and pk to use as arguments in other views.
        """
        if "slug" in self.kwargs:
            return get_object_or_404(Post, slug=self.kwargs["slug"])
        elif "pk" in self.kwargs:
            return get_object_or_404(Post, pk=self.kwargs["pk"])

    def post(self, request, *args, **kwargs):
        """
        Handles the like button.
        Toggles like and unlike.
        Method decorator ensures that only logged in users can like.
        """
        post = self.get_object()
        if request.user.is_authenticated:
            if request.user in post.likes.all():
                post.likes.remove(request.user)
                messages.success(request, "You have unliked this post.")
            else:
                post.likes.add(request.user)
                messages.success(
                    request, "You have liked this post."
                )
        return HttpResponseRedirect(
            reverse("post_detail", kwargs={"slug": post.slug})
        )


class AddPost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Display Add Post view
    LoginRequiredMixin checks if user is logged in before running CreateView,
        redirects user to login page, if user is not logged in
    CreateView handles form to add a post in the DOM
    Related to :model:`board.Post`
    **Context**
    ``post``
        An instance of :model:`board.Post`.
    ***Template:***
    :template:`board/add_post.html`
    """

    template_name = "board/add_post.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("board")
    success_message = "You successfully pinned your post to the board!"

    def form_valid(self, form):
        """
        Defines the author of the post.
        Prevents user being able to choose other usernames as author.
        Delay saving post to database: check if image was upoloaded,
            else save post_image as None to database.
        """
        form.instance.author = self.request.user
        post = form.save(commit=False)
        if self.request.FILES.get("post_image"):
            post.post_image = self.request.FILES["post_image"]
        else:
            post.post_image = None
        post.save()
        return super().form_valid(form)


class EditPost(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    """
    Edit user's own content.
    Utilizes Django's authentication system's mixins
        to secure edit of only own content
    Related to :model:`board.Post`
    **Context**
    ``post``
        An instance of :model:`board.Post`.
    #``slug``
    #    Assigning the slug to a variable for redirecting.
    ***Template:***
    :template:`board/edit_post.html`
    """

    template_name = "board/edit_post.html"
    model = Post
    form_class = PostForm
    success_message = "You successfully updated your post!"

    def test_func(self):
        """
        Required for UserPassesTextMixin.
        Returns True if user passes test: is content author.
        Returns False if user is not content author and throws 403 error.
        """
        return self.request.user == self.get_object().author

    def form_valid(self, form):
        """
        Saves changes in form after editing.
        Redirects to board after updating.
        """
        response = super().form_valid(form)
        return response

    def get_context_data(self, **kwargs):
        """
        Updates post.
        """
        # kwargs.update({"post": self.object})
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse("post_detail", kwargs={"slug": self.object.slug})


class DeletePost(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    """
    Delete user's own content.
    Utilizes Django's authentication system's mixins
        to secure deletion of only own content
    Utilizes Django's built-in deletion logic
    Related to :model:`board.Post`
    ***Template:***
    :template:`board/post_confirm_delete.html`
    """

    template_name = "board/post_confirm_delete.html"
    model = Post
    success_url = reverse_lazy("board")
    success_message = "You successfully deleted your post!"

    def test_func(self):
        """
        Required for UserPassesTextMixin.
        Returns True if user passes test: is content author.
        Returns False if user is not content author and throws 403 error.
        """
        return self.request.user == self.get_object().author
