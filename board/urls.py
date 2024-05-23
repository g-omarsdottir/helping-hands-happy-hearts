from django.urls import path
from . import views
from .views import AddPost, Board, PostDetail, DeletePost, EditPost, AddComment


urlpatterns = [
    path("add/", AddPost.as_view(), name="add_post"),
    path("board/", views.Board.as_view(), name="board"),
    path("post/<slug:slug>/", PostDetail.as_view(), name="post_detail"),
    path("delete/<slug:slug>/", DeletePost.as_view(), name="delete_post"),
    path("edit/<slug:slug>/", EditPost.as_view(), name="edit_post"),
    path("post/<slug:slug>/", AddComment.as_view(), name="add_comment"),
]
