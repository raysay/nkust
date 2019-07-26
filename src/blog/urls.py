from django.contrib import admin
from django.urls import path,include,re_path
from . import views

app_name = 'blog'

urlpatterns = [
    # path('home/', views.as_view(), name='home'),
    path('post/', views.post, name='post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
]
