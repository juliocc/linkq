from django.db import models
from model_utils.models import TimeStampedModel
from model_utils.managers import QueryManager
from tinymce import models as tinymce_models


class Link(TimeStampedModel):
    url = models.CharField("URL", max_length=1024, unique=True)
    read = models.DateTimeField("Date read", null=True, blank=True)
    summary = tinymce_models.HTMLField(blank=True)

    # TODO: add title

    objects = models.Manager()
    objects_read = QueryManager(read__isnull=False).order_by('created')
    objects_unread = QueryManager(read__isnull=True).order_by('created')

    def __unicode__(self):
        return self.url
