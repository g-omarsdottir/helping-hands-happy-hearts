from django.urls import path
from . import views
from .views import AddPost, Board


urlpatterns = [
    path('add/', AddPost.as_view(), name='add_post'),
    path('board/', views.Board.as_view(), name='board'),
]
