from django.db import models
from model_utils.models import TimeStampedModel
from model_utils.managers import QueryManager

from djorm_pgfulltext.models import SearchManager
from djorm_pgfulltext.fields import VectorField
from taggit_autosuggest_select2.managers import TaggableManager
from tinymce import models as tinymce_models
from south.modelsinspector import add_ignored_fields

add_ignored_fields(["^taggit_autosuggest_select2\.managers"])

class Link(TimeStampedModel):
    url = models.CharField("URL", max_length=1024, unique=True)
    read = models.DateTimeField("Date read", null=True, blank=True)
    summary = tinymce_models.HTMLField(blank=True)
    title = models.CharField("Title", max_length=1024, blank=True)
    search_index = VectorField()

    objects = SearchManager(
        fields = ('title', 'summary'),
        config = 'pg_catalog.english',   # this is default
        search_field = 'search_index',   # this is default
        auto_update_search_field = False # we do it using a trigger
    )

    objects_read = QueryManager(read__isnull=False).order_by('created')
    objects_unread = QueryManager(read__isnull=True).order_by('created')

    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.url
