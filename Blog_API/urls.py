from .views import *
from django.urls import path
from .views import CreatePostView, UpdatePostView

app_name = 'Blog_API'

urlpatterns = [
    path('create/', CreatePostView.as_view(), name='create-post'),
    path('update/<int:pk>/', UpdatePostView.as_view(), name='update-post'),
    path('<int:pk>/', DeletePostView.as_view(), name='delete-post'),
    path('post/<int:pk>/', GetPostView.as_view(), name='get-post'),
    path('all/', GetAllPostsView.as_view(), name='get-all-posts'),
    path('blog-posts/', GetAllPostsView.as_view(), name='get-all-blog-posts'),
]
