from django.conf.urls import patterns, url
from .views import (
	PostCreateAPIView,
	PostListAPIView,
	PostDetailAPIView,
	PostUpdateAPIView,
	PostDeleteAPIView,
	)


urlpatterns =[
        url(r'^$', PostListAPIView.as_view(), name='list'),
        # url(r'^category/(?P<category_name_slug>[\w\-]+)/$', category, name='category'),
        url(r'^post/(?P<slug>[\w\-]+)/$', PostDetailAPIView.as_view(), name='post_detail'),
        url(r'^add/$', PostCreateAPIView.as_view(), name='create'),
        url(r'^post/(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
        url(r'^post/(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),

]

