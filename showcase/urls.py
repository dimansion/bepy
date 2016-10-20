from django.conf.urls import patterns, url
from .views import (
	student_list,

	)

urlpatterns = [ 
        url(r'^$', student_list, name='student_list'),

]
