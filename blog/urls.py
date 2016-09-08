from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^post/(?P<post_title_slug>[\w\-]+)/$', views.post_detail, name='post_detail'),


)
