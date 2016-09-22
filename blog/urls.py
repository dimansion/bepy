from django.conf.urls import patterns, url
from .views import (
	index,
	category,
	post_detail,

	)


urlpatterns = patterns('',
        url(r'^$', index, name='index'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', category, name='category'),
        url(r'^post/(?P<post_title_slug>[\w\-]+)/$', post_detail, name='post_detail'),


)
