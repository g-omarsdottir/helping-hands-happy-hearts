from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm


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
    and :model:`board.Comment`
    **Context**
    Context object name customized for readability.
    ``post``
        An instance of :model:`board.Post`
    ``queryset``
        All published instances of :model:`bord.Post`
    ``comments``
        All comments related to the post
    ``comment_count``
        A count of comments related to the post
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
        if 'slug' in self.kwargs:
            return get_object_or_404(Post, slug=self.kwargs['slug'])
        elif 'pk' in self.kwargs:
            return get_object_or_404(Post, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context["comments"] = Comment.objects.filter(post=post)
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comments.all().order_by("-published_date")
        comment_count = post.comments.count()
        context["comments"] = comments
        context["comment_count"] = comment_count
        return context


class AddPost(LoginRequiredMixin, CreateView):
    """
    Display Add Post view
    LoginRequiredMixin checks if user is logged in before running CreateView
    If user is not logged in and attempts to add post, it redirects user to login page
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
        messages.success(
            self.request, "You successfully pinned your post to the board!"
        )
        return super().form_valid(form)


class EditPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit user's own content.
    Utilizes Django's authentication system's mixins to secure edit of only own content.
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
        Redirects to board after updating (like in codestar walkthrough project).
        """
        response = super().form_valid(form)
        messages.success(self.request, "You successfully updated your post!")
        return response

    def get_context_data(self, **kwargs):
        """
        Updates post.
        """
        kwargs.update({"post": self.object})
        return super(EditPost, self).get_context_data(**kwargs)

    def get_success_url(self):
        return reverse("post_detail", kwargs={"slug": self.object.slug})


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete user's own content.
    Utilizes Django's authentication system's mixins to secure deletion of only own content.
    Utilizes Django's built-in deletion logic.
    Related to :model:`board.Post`
    ***Template:***
    :template:`board/post_confirm_delete.html`
    """

    template_name = "board/post_confirm_delete.html"
    model = Post
    success_url = reverse_lazy("board")

    def test_func(self):
        """
        Required for UserPassesTextMixin.
        Returns True if user passes test: is content author.
        Returns False if user is not content author and throws 403 error.
        """
        return self.request.user == self.get_object().author


class AddComment(LoginRequiredMixin, CreateView):
    """
    Creates a comment to a specific post
    Display Add Comment view and handles creating a comment
    LoginRequiredMixin checks if user is logged in before running CreateView
    If user is not logged in and attempts to add post, it redirects user to login page
    CreateView handles form to add a post in the DOM
    Related to :model:`board.Comment`
    **Context**
    Context object name customized for readability
    ``queryset``
        All comments related to a single post
    ***Template:***
    :template:`board/post_detail.html`
    ``comment_form``
        An instance of :form:`board.CommentForm`
    ``post``
        An instance of :model:`board.Post`
    """

    template_name = "board/post_detail.html"
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        """
        Handles form submission to add comment
        Provides success message as user feedback
        """
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        form.instance.author = self.request.user
        form.instance.post = post
        messages.success(self.request, "Your comment has been posted!")
        return super().form_valid(form)

    def get_success_url(self):
        """
        Returns URL to redirect to after a successfully adding comment.
        """
        return reverse_lazy("post_detail", kwargs={"pk": self.object.post.pk})
