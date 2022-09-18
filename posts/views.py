from django.shortcuts import render
from django.views import generic
from .models import Post, PostView, Like, Comments
from .forms import PostForm

# Create your views here.

class PostListView(generic.ListView):
    model = Post

class PostDetailView(generic.DetailView):
    model = Post

class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'Create'
        })
        return context
    
    success_url = '/'
   

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type':'Update'
        })
        return context
    
    success_url = '/'
   
    
class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = '/'