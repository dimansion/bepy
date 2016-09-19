from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings # New Import
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^project/', include('project.urls')),
    url(r'^register/$', 'blog.views.register', name='register'),
    url(r'^login/$', auth_view.login, name='login', kwargs={'template_name': 'users/login.html'}),
    url(r'^logout/$', auth_view.logout, name='logout', kwargs={'next_page': '/blog'}),
    url(r'^success/$', 'blog.views.register_success'),    
    url(r'^confirm/(?P<activation_key>\w+)/$', 'blog.views.confirm'),  

]
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )