from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings # New Import
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_view
from blog.views import AboutView, HomeView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='index'), 
    url(r'^blog/', include('blog.urls')),
    url(r'^project/', include('project.urls')),
    url(r'^logout/$', auth_view.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^about/$', AboutView.as_view()),   
    #url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/', include('allauth.urls')),
      
]
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )