# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Link'
        db.create_table(u'links_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('read', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('summary', self.gf('tinymce.models.HTMLField')(blank=True)),
        ))
        db.send_create_signal(u'links', ['Link'])


    def backwards(self, orm):
        # Deleting model 'Link'
        db.delete_table(u'links_link')


    models = {
        u'links.link': {
            'Meta': {'object_name': 'Link'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'read': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'summary': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['links']