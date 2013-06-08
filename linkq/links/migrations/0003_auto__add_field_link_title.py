# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Link.title'
        db.add_column(u'links_link', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1024, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Link.title'
        db.delete_column(u'links_link', 'title')


    models = {
        u'links.link': {
            'Meta': {'object_name': 'Link'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'read': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'summary': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1024'})
        }
    }

    complete_apps = ['links']