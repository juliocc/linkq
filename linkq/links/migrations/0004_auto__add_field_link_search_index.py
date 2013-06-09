# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Link.search_index'
        db.add_column(u'links_link', 'search_index',
                      self.gf('djorm_pgfulltext.fields.VectorField')(default='', null=True, db_index=True),
                      keep_default=False)
        db.execute("""
        CREATE INDEX links_link_search_index_index ON links_link USING gin(search_index);
        CREATE TRIGGER update_links_link_search_index
          BEFORE INSERT OR UPDATE ON links_link
          FOR EACH ROW EXECUTE PROCEDURE
          tsvector_update_trigger(search_index, 'pg_catalog.english', title, summary);
        UPDATE links_link SET title=title; -- populate search_index
        """)



    def backwards(self, orm):
        db.execute("DROP INDEX links_link_search_index_index;")
        db.execute("DROP TRIGGER update_links_link_search_index ON links_link;")
        db.delete_column(u'links_link', 'search_index')

    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'links.link': {
            'Meta': {'object_name': 'Link'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'read': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'search_index': ('djorm_pgfulltext.fields.VectorField', [], {'default': "''", 'null': 'True', 'db_index': 'True'}),
            'summary': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1024'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        }
    }

    complete_apps = ['links']
