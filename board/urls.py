from django.urls import path
from . import views
from .views import AddPost, Board, PostDetail, DeletePost, EditPost


urlpatterns = [
    path("add/", views.AddPost.as_view(), name="add_post"),
    path("board/", views.Board.as_view(), name="board"),
    path("post/<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path("delete/<slug:slug>/", views.DeletePost.as_view(), name="delete_post"),
    path("edit/<slug:slug>/", views.EditPost.as_view(), name="edit_post"),
    path(
        "posts/<slug:slug>/<int:pk>/like/", views.PostDetail.as_view(), name="like_post"
    ),
]
