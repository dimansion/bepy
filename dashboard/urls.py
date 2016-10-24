from django.conf.urls import patterns, url
from .views import (
	user_dashboard,
	user_update,
	user_project,
	add_project,
	user_project_detail,
	user_project_update,
	user_project_delete,

	)

urlpatterns = [ 
        url(r'^$', user_dashboard, name='user_dashboard'),
        url(r'^(?P<slug>[\w-]+)/edit/$', user_update, name='update'),
        url(r'^projects$', user_project, name='projects'),
        url(r'^add/$', add_project, name='add_project'),
        url(r'^project/(?P<user_project_slug>[\w\-]+)/$', user_project_detail, name='project_detail'),
        url(r'^project/(?P<slug>[\w-]+)/edit/$', user_project_update, name='update_project'),
        url(r'^project/(?P<slug>[\w-]+)/delete/$', user_project_delete, name='delete'),


]
