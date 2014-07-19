from django.conf.urls import patterns, url
from blockbuilder.views import PhraseCreate, PhraseDetailView

urlpatterns = patterns('',
    url(r'^phrase/$', PhraseCreate.as_view(), name='phrase'),
    url(r'^phrase/(?P<pk>\d+)$', PhraseDetailView.as_view(), name='phrase-detail'),
)