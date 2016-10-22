from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings # New Import
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_view
from blog.views import AboutView, HomeView, ContactView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', AboutView.as_view(), name='about'), 
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^api/blog/', include('blog.api.urls', namespace='blog-api')),
    url(r'^blog/', include('article.urls', namespace='blog')),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')), 
    url(r'^logout/$', auth_view.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^showcase/', include('showcase.urls', namespace='showcase')),
    url(r'^project/step/', include('blog.urls')),
    url(r'^project/', include('project.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)