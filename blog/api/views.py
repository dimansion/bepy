from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	RetrieveAPIView,
	UpdateAPIView,
	)

from blog.models import Post
from .serializers import (
	PostDetailSerializer, 
	PostListSerializer,
	PostCreateUpdateSerializer,
	)

class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer

class PostListAPIView(ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer

class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer	
	lookup_field = 'slug'

class PostUpdateAPIView(UpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	lookup_field = 'slug'

class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'