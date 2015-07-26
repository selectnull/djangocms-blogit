# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from blogit.models import Post, Tag, Category, PostList
from blogit.utils import paginate_queryset


class PostListPlugin(CMSPluginBase):
    model = PostList
    module = "Blogit"
    name = "Post List"
    render_template = "blogit/plugins/post_list.html"

    def render(self, context, instance, placeholder):
        request = context['request']
        qs = Post.objects.published(request)
        filters = {}
        if instance.filter_by_author:
            filters['author'] = instance.filter_by_author
        if instance.filter_by_category:
            filters['category'] = instance.filter_by_category
        if instance.filter_by_tags.count() > 0:
            filters['tags'] = instance.filter_by_tags.all()
        if filters:
            qs = qs.filter(**filters)
        print filters
        paginator, page, queryset, is_paginated = paginate_queryset(
            qs, request.GET.get('page', 1), instance.show_paginator,
            instance.number_of_posts, instance.orphans)
        context.update({
            'paginator': paginator,
            'page_obj': page,
            'is_paginated': is_paginated and instance.show_paginator,
            'object_list': queryset
        })
        return context

    def get_render_template(self, context, instance, placeholder):
        return instance.template_name or self.render_template


class TagListPlugin(CMSPluginBase):
    model = CMSPlugin
    module = "Blogit"
    name = "Tag List"
    render_template = "blogit/plugins/tag_list.html"

    def render(self, context, instance, placeholder):
        context.update({'object_list': Tag.objects.filter(active=True)})
        return context


class CategoryListPlugin(CMSPluginBase):
    model = CMSPlugin
    module = "Blogit"
    name = "Category List"
    render_template = "blogit/plugins/category_list.html"

    def render(self, context, instance, placeholder):
        context.update({'object_list': Category.objects.filter(active=True)})
        return context


plugin_pool.register_plugin(PostListPlugin)
plugin_pool.register_plugin(TagListPlugin)
plugin_pool.register_plugin(CategoryListPlugin)
