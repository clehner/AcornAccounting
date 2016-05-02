# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        from django.core.management import call_command
        call_command('loaddata', 'accounts/fixtures/accounts_acorn_headers.json')
