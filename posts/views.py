from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
    )
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy


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
    fields = ['title', 'subtitle', 'body', 'status']

    def form_valid(self, form):
        # Set the author of the post to the current user
        form.instance.author = User.objects.last() # Get the last user in the database
        return super().form_valid(form)

class PostUpdateView(UpdateView): #POST Request -> Update object / pre-filled form (html)
    template_name = 'posts/edit.html'
    model = Post
    fields = ['title', 'subtitle', 'body', 'status']

class PostDeleteView(DeleteView): #POST Request -> Delete object
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('post_list') # Redirect to the post list view after deletion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        print(self.get_object())
        return context