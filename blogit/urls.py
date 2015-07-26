# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url
from django.utils.translation import ugettext_lazy as _

from blogit import settings as bs
from blogit.views import (
    CategoryListView, CategoryDetailView,
    TagListView, TagDetailView,
    PostYearArchiveView, PostMonthArchiveView, PostDayArchiveView,
    PostListView, PostDetailView, PostDateDetailView)
from blogit.feeds import PostRssFeed, PostAtomFeed


pats = []
if bs.USE_BUILTIN_LIST_VIEW:
    pats.append(url(r'^$', PostListView.as_view(), name='blogit_post_list'))

pats.extend([
    url(r'^(?P<year>\d+)/(?P<month>[-\w\d]+)/(?P<day>\d+)/$',
        PostDayArchiveView.as_view(), name='blogit_post_archive_day'),
    url(r'^(?P<year>\d+)/(?P<month>[-\w\d]+)/$',
        PostMonthArchiveView.as_view(), name='blogit_post_archive_month'),
    url(r'^(?P<year>\d+)/$', PostYearArchiveView.as_view(),
        name='blogit_post_archive_year'),

    url(_(r'^categories/$'),
        CategoryListView.as_view(), name='blogit_category_list'),
    url(_(r'^categories/(?P<slug>[-\w\d]+)/$'),
        CategoryDetailView.as_view(), name='blogit_category_detail'),

    url(_(r'^tags/$'), TagListView.as_view(), name='blogit_tag_list'),
    url(_(r'^tags/(?P<slug>[-\w\d]+)/$'),
        TagDetailView.as_view(), name='blogit_tag_detail'),
])

if bs.RSS_FEED:
    pats.extend([
        url(_(r'^feeds/rss/$'), PostRssFeed()),
        url(_(r'^feeds/rss/(?P<tag_slug>[-\w]+)/$'), PostRssFeed()),
    ])

if bs.ATOM_FEED:
    pats.extend([
        url(_(r'^feeds/atom/(?P<tag_slug>[-\w]+)/$'), PostAtomFeed()),
        url(_(r'^feeds/atom/$'), PostAtomFeed()),
    ])


pats.extend([
    url(r'^(?P<year>\d+)/(?P<month>[-\w\d]+)/(?P<day>\d+)'
        r'/(?P<slug>[-\w\d]+)/$', PostDateDetailView.as_view(),
        name='blogit_post_detail_date'),
    url(r'^(?P<slug>[-\w\d]+)/$', PostDetailView.as_view(),
        name='blogit_post_detail'),
])


urlpatterns = patterns('', *pats)
