from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, ListAPIView
from .models import Post
from .serializers import PostSerializer


class CreatePostView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UpdatePostView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DeletePostView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GetPostView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GetAllPostsView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class SearchPostsView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter = [SearchFilter]
    search_fields = ['title', 'content', 'tags']
