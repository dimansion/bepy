from django.conf.urls import patterns, url
from .views import (
	index,
	category,
	post_detail,
	post_create,
	post_update,
	post_delete,

	)


urlpatterns =[
        url(r'^$', index, name='index'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', category, name='category'),
        url(r'^post/(?P<slug>[\w\-]+)/$', post_detail, name='post_detail'),
        url(r'^add/$', post_create),
        url(r'^post/(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
        url(r'^post/(?P<slug>[\w-]+)/delete/$', post_delete),

]

