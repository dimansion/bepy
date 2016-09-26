from django.conf.urls import patterns, url
from .views import (
	page_list,
	page_detail,
	lesson_detail,

	)

urlpatterns = [
        url(r'^$', page_list, name='page_list'),
        url(r'^(?P<page_title_slug>[\w\-]+)/$', page_detail, name='page_detail'),
        url(r'^lessons/(?P<lesson_name_slug>[\w\-]+)/$', lesson_detail, name='lesson_detail'),
       
]
