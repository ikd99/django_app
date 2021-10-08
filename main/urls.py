from django.urls import path
from . import views

app_name='main'
urlpatterns = [
  path('', views.index, name='index'),
  path('chat/<int:num>', views.chat, name='chat'),
  path('post/', views.post, name='post'),
]

