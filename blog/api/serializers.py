from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	) 

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

post_detail_url = HyperlinkedIdentityField(
	view_name='blog-api:post_detail',
	lookup_field='slug',

	)
class PostListSerializer(ModelSerializer):
	url = post_detail_url
	author = SerializerMethodField()
	class Meta:
		model = Post
		fields = [
			'url',
			'author',
			'title',
			'slug',
			'content',
		]

	def get_author(self, obj):
		return str(obj.author.username)	

class PostDetailSerializer(ModelSerializer):
	url = post_detail_url
	author = SerializerMethodField()
	class Meta:
		model = Post
		fields = [
			'url',
			'id',
			'author',
			'title',
			'slug',
			'content',
		]

	def get_author(self, obj):
		return str(obj.author.username)	

#this is for project app
#image = SerializerMethodField()

#def get_image(self, obj):
	# try:
	# 	image = obj.image.url
	# except:
	# 	image = None
	# return image		
