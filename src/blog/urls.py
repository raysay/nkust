from django.contrib import admin
from django.urls import path,include,re_path
from . import views

appname='post'
urlpatterns = [

    # path('home/', views.as_view(), name='home'),
    path('post/', views.post, name='post'),
    path('post/<int:blog>/', views.post_detail, name='post_detail'),
]
