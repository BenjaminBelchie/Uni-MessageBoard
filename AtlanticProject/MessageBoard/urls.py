from django.urls import path
from .views import PostListViewD, PostListViewA,PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, UserListAll
from . import views

#This is another URL handling doucment and all the URLS here are from the /MessageBoard URL, for exmaple clicking New Post on the nav bar would be handled here and not in the project wide URLS. 
#Keeping different scopes for different URLS helps possible interferience and also makes the program more efficant and robust as these URLS can only be accessed from the main dashboard. 
urlpatterns = [
    path('', PostListViewD.as_view(), name='MessageBoard-home'),
    path('post/a', PostListViewA.as_view(), name='MessageBoard-home-acending'),
    path('user/all', UserListAll.as_view(), name='users-list'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='MessageBoard-about'),
    path('search/', views.get_queryset, name='MessageBoard-search'),
]