from django.conf.urls import patterns, include, url
from django.contrib import admin

from blockbuildersite.views import AboutView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', AboutView.as_view()),
    url(r'^blockbuilder/', include('blockbuilder.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
