from dataclasses import field
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from app_blog.models import Post
from .forms import PostForm,EditForm
# Create your views here.

#def home(request):
 #   return render(request,'app_blog/home.html',{})

class HomeView(ListView):
    model=Post
    template_name='app_blog/home.html'
    ordering=['-id']
    

class ArticleDetailView(DetailView):
    model=Post
    template_name='app_blog/article_detail.html'

class AddPostView(CreateView):
    model=Post
    form_class= PostForm
    template_name='app_blog/add_post.html'
    #fields='__all__'
    #fields=('title','body')

class UpdatePostView(UpdateView):
    model=Post
    form_class=EditForm
    template_name='app_blog/update_post.html'
    #fields=['title','title_tag','body']

class DeletePostView(DeleteView):
    model=Post
    template_name='app_blog/delete_post.html'