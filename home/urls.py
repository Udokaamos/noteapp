from django.urls import path, reverse_lazy
from .views import PostListView, PostCreateView, PostDetailView
from . import views


# app_name='home'
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/create',
        PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>', 
        views.PostDetailView.as_view(), name='post_detail'),
    # path('ad/create',
    #     views.AdCreateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_create'),
   
]
