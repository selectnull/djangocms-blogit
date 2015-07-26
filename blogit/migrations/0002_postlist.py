# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostList',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('number_of_posts', models.IntegerField(default=10)),
                ('show_paginator', models.BooleanField(default=True)),
                ('orphans', models.IntegerField(default=0)),
                ('template_name', models.CharField(help_text='Select a template or leave empty for default one.', max_length=200, blank=True)),
                ('filter_by_author', models.ForeignKey(related_name='filtered_by_author', blank=True, to=settings.AUTH_USER_MODEL, help_text='Filter by author or leave blank for all authors.', null=True, verbose_name='Filter by author')),
                ('filter_by_category', mptt.fields.TreeForeignKey(related_name='filtered_by_category', blank=True, to='blogit.Category', help_text='Filter by category or leave blank for all categories.', null=True, verbose_name='Category')),
                ('filter_by_tags', models.ManyToManyField(related_name='filtered_by_tags', to='blogit.Tag', blank=True, help_text='Filter by tags (one or more) or leave blank for all tags.', null=True, verbose_name='Tags')),
            ],
            options={
                'db_table': 'blogit_post_lists',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
