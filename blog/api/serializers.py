from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from blog.models import Post

class PostCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'title',
			#'slug',
			'content',
			'published_date',

		]	

class PostListSerializer(ModelSerializer):
	author = serializers.SlugRelatedField(slug_field='username',read_only=True)
	class Meta:
		model = Post
		fields = [
			'author',
			'title',
			'slug',
			'content',
		]

class PostDetailSerializer(ModelSerializer):
	author = serializers.SlugRelatedField(slug_field='username',read_only=True)
	class Meta:
		model = Post
		fields = [
			'id',
			'author',
			'title',
			'slug',
			'content',
		]

