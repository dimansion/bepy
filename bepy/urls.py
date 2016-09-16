from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings # New Import
from django.conf.urls.static import static # New Import

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^project/', include('project.urls')),
]
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )