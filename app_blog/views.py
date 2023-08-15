from dataclasses import field
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from app_blog.models import Post, Category
from .forms import PostForm,EditForm
from django.urls import reverse_lazy
# Create your views here.

#def home(request):
 #   return render(request,'app_blog/home.html',{})

class HomeView(ListView):
    model=Post
    template_name='app_blog/home.html'
    ordering=['-created']
    
class ArticleDetailView(DetailView):
    model=Post
    template_name='app_blog/article_detail.html'

class AddPostView(CreateView):
    model=Post
    form_class= PostForm
    template_name='app_blog/add_post.html'
    #fields='__all__'
    #fields=('title','body')

class AddCategoryView(CreateView):
    model=Category
    #form_class= PostForm
    template_name='app_blog/add_category.html'
    fields='__all__'
    #fields=('title','body')

class UpdatePostView(UpdateView):
    model=Post
    form_class=EditForm
    template_name='app_blog/update_post.html'
    #fields=['title','title_tag','body']

class DeletePostView(DeleteView):
    model=Post
    template_name='app_blog/delete_post.html'
    success_url=reverse_lazy('home')

def CategoryView(request,cats):
    category_posts=Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'app_blog/categories.html', {'cats':cats.replace('-',' '), 'category_posts':category_posts})    