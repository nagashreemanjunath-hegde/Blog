from django.urls import path
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,LikeView,DeletePostView,AddCategoryView,CategoryView,CategoryListView

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('article_detail/<int:pk>',ArticleDetailView.as_view(),name="article-detail"),
    path('add_post/',AddPostView.as_view(),name="add-post"),
    path('add_category/',AddCategoryView.as_view(),name="add-category"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name="update-post"),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name="delete-post"),
    path('category/<str:cats>/', CategoryView,name='category'),
    path('category-list/', CategoryListView,name='category-list'),
    path('like/<int:pk>',LikeView,name='like-post'),
]
