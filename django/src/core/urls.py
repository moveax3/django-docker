from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from filebrowser.sites import site

urlpatterns = [
    url(r'^sitemap\.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='text/xml; charset=utf-8'),
        name="sitemap.xml"),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name="robots.txt"),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^realadmin/', include(admin.site.urls)),  # admin
    url(r'^realadmin/filebrowser/', include(site.urls)),  # admin
    url(r'^realadmin/defender/', include('defender.urls')),
    url(r'session_security/', include('session_security.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

#handler404 = 'core.views.error_404'

urlpatterns += [
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
            url(r'^__debug__/', include(debug_toolbar.urls)),
    )
