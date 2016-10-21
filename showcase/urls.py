from django.conf.urls import patterns, url
from .views import (
	student_list,
	student_detail,
	student_project_detail,

	)

urlpatterns = [ 
        url(r'^$', student_list, name='student_list'),
        url(r'^(?P<user_slug>[\w\-]+)/$', student_detail, name='student_detail'),
        url(r'^(?P<user_slug>[\w\-]+)/(?P<student_project_slug>[\w\-]+)/$', student_project_detail, name='student_project_detail'),
       
]
