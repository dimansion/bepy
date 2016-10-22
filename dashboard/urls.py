from django.conf.urls import patterns, url
from .views import (
	user_dashboard,

	)

urlpatterns = [ 
        url(r'^$', user_dashboard, name='user_dashboard'),
]
