from django.conf.urls import patterns, url
from project import views

urlpatterns = patterns('',
        url(r'^$', views.page_list, name='page_list'),
        url(r'^project/(?P<page_title_slug>[\w\-]+)/$', views.page_detail, name='page_detail'),
        url(r'^(?P<lesson_name_slug>[\w\-]+)/$', views.lesson_detail, name='lesson_detail'),
       
)
