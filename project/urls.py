from django.conf.urls import patterns, url
from .views import (
	page_list,
	page_detail,
	lesson_detail,
	ProjectView,

	)

urlpatterns = [
		url(r'^$', ProjectView.as_view(), name='project'),  
        url(r'^video/$', page_list, name='page_list'),
        url(r'^(?P<page_title_slug>[\w\-]+)/$', page_detail, name='page_detail'),
        url(r'^video/(?P<lesson_name_slug>[\w\-]+)/$', lesson_detail, name='lesson_detail'),
       
]
