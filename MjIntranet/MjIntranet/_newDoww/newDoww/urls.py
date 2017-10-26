from django.conf.urls import include, url
from django.contrib import admin
from mainSection import views
from django.conf import settings



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.render_doww),
    url(r'^mainSection/', include('mainSection.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]