from django.urls import path
from . import views
from .views import AddPost


urlpatterns = [
    path('add/', AddPost.as_view(), name='add_post'),
    path('', views.BoardView.as_view(), name='board'),
]
