from dataclasses import field
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from app_blog.models import Post
from .forms import PostForm
# Create your views here.

#def home(request):
 #   return render(request,'app_blog/home.html',{})

class HomeView(ListView):
    model=Post
    template_name='app_blog/home.html'
    

class ArticleDetailView(DetailView):
    model=Post
    template_name='app_blog/article_detail.html'

class AddPostView(CreateView):
    model=Post
    form_class= PostForm
    template_name='app_blog/add_post.html'
    #fields='__all__'
    #fields=('title','body')

   
