from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from blog.models import Post

class PostSerializer(ModelSerializer):
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