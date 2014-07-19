from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from blockbuildersite.views import AboutView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', AboutView.as_view()),
    url(r'^blockbuilder/', include('blockbuilder.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
