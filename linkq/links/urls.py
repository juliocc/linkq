from django.conf.urls import patterns, include, url

from .views import AddLinkView, QueuedLinksView, ReadLinksView

urlpatterns = patterns('',
    url(r'^add$', AddLinkView.as_view(), name='add_links'),
    url(r'^queued$', QueuedLinksView.as_view(), name='queued_links'),
    url(r'^read$', ReadLinksView.as_view(), name='read_links'),
)
