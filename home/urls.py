from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView
#  PostUpdateView, PostDeleteView
from . import views


# app_name='home'
urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/create/',
        PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>', 
        PostDetailView.as_view(), name='post_detail'),
    # path('post/<int:pk>/update/', PostUpdateView.as_view(success_url=reverse_lazy('home:all')), name='post_update'),
    # path('post/<int:pk>/delete/', PostDeleteView.as_view(success_url=reverse_lazy('home:all')), name='post_delete'),
    # # path('ad/create',
    #     views.AdCreateView.as_view(success_url=reverse_lazy('ads:all')), name='ad_create'),
   
]

# urlpatterns = [
#     path('', views.home, name = 'base'),
#     path('new_post', views.new_post, name = 'new'),
#     path('post/<str:pk>', views.post_detail, name = 'post'),
#     # path('delete_note/<str:pk>', views.delete_note, name = 'delete'),
#     # path('search_result', views.search_page, name = 'search'),

# ]
