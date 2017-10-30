from django.conf.urls import include, url
from django.contrib import admin
from mainSection import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.render_doww),
    url(r'^(?P<id>\d+)$', views.list_contents),
    url(r'^mainSection/', include('mainSection.urls')),
    url(r'^loginapp/', include('loginapp.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]