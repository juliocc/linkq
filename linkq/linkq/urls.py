from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from links.views import NextLinkView

urlpatterns = patterns('',
    url(r'^$', NextLinkView.as_view(), name='index'),

    # Examples:
    # url(r'^$', 'linkq.views.home', name='home'),
    url(r'^links/', include('links.urls')),

    # uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^taggit_autosuggest/', include('taggit_autosuggest_select2.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
