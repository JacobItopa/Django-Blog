from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post, PostView, Like, Comments, User
from .forms import PostForm

# Create your views here.

class PostListView(generic.ListView):
    model = Post

class PostDetailView(generic.DetailView):
    model = Post

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=object)
        return object

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

    

def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail', slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail', slug=slug)
