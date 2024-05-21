from django.urls import path
from . import views
from .views import AddPost, Board, PostDetail, DeletePost


urlpatterns = [
    path("add/", AddPost.as_view(), name="add_post"),
    path("board/", views.Board.as_view(), name="board"),
    path("<slug:pk>/", PostDetail.as_view(), name="post_detail"),
    path("delete/<slug:pk>/", DeletePost.as_view(), name="delete_post"),
]
