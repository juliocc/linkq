# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Link', fields ['url']
        db.create_unique(u'links_link', ['url'])


    def backwards(self, orm):
        # Removing unique constraint on 'Link', fields ['url']
        db.delete_unique(u'links_link', ['url'])


    models = {
        u'links.link': {
            'Meta': {'object_name': 'Link'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'read': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'summary': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1024'})
        }
    }

    complete_apps = ['links']