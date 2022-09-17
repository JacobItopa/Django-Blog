from django.shortcuts import render
from django.views import generic
from .models import Post, PostView, Like, Comments

# Create your views here.

class PostListView(generic.ListView):
    model = Post

class PostDetailView(generic.DetailView):
    model = Post

class PostCreateView(generic.CreateView):
    model = Post
    fields = (
        'title',
        'content',
        'thumbnail',
        'author',
        'slug'
    )

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = (
        'title',
        'content',
        'thumbnail',
        'author',
        'slug'
    )
    
class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = '/'