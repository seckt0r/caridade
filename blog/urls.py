from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blogListView.as_view(), name='blog_list'),
    path('<slug:slug>/', views.blogDetailView.as_view(), name='blog_detail'),
]
