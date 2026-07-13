from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
    )
from .models import Post

# Create your views here.
class PostListView(ListView): #GET Request -> List
    # Templatr_name attribute renders a specific html file
    template_name = 'posts/list.html'
    # model attribute specifies which model to use for the view
    model = Post
    # contect_object_name attribute specifies the name of the context variable to use in the template
    context_object_name = 'posts'

class PostDetailView(DetailView): #GET Request -> single object
    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'single_post' 

class PostCreateView(CreateView): #POST Request -> New object / empty form (html)
    template_name = 'posts/new.html'
    model = Post
    fields = ['title', 'subtitle', 'body', 'author']
