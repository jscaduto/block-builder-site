from django.conf.urls import patterns, url
from blockbuilder.views import PhraseCreate, PhraseDetailView, get_lastest_phrases

urlpatterns = patterns('',
    url(r'^api/latest-phrases/$', get_lastest_phrases),
    url(r'^phrase/$', PhraseCreate.as_view(), name='phrase'),
    url(r'^phrase/(?P<pk>\d+)$', PhraseDetailView.as_view(), name='phrase-detail'),
)
