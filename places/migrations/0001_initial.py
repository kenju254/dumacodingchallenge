# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'County'
        db.create_table(u'places_county', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('num', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
        ))
        db.send_create_signal(u'places', ['County'])

        # Adding model 'Ward'
        db.create_table(u'places_ward', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('num', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('county', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.County'])),
        ))
        db.send_create_signal(u'places', ['Ward'])

        # Adding model 'Location'
        db.create_table(u'places_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('num', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(default='0.000000', max_length=255, blank=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(default='0.000000', max_length=255, blank=True)),
            ('ward', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['places.Ward'])),
        ))
        db.send_create_signal(u'places', ['Location'])


    def backwards(self, orm):
        # Deleting model 'County'
        db.delete_table(u'places_county')

        # Deleting model 'Ward'
        db.delete_table(u'places_ward')

        # Deleting model 'Location'
        db.delete_table(u'places_location')


    models = {
        u'places.county': {
            'Meta': {'object_name': 'County'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'num': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        },
        u'places.location': {
            'Meta': {'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'default': "'0.000000'", 'max_length': '255', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'default': "'0.000000'", 'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'num': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'ward': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.Ward']"})
        },
        u'places.ward': {
            'Meta': {'object_name': 'Ward'},
            'county': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['places.County']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'num': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['places']