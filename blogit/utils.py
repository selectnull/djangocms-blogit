# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.template import RequestContext
from django.utils.html import strip_tags
try:
    from django.utils.encoding import force_unicode
except ImportError:
    from django.utils.encoding import force_text as force_unicode
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404
from django.utils.translation import ugettext_lazy as _

from cms.utils.i18n import get_current_language


def get_request(language=None):
    """
    Returns a Request instance populated with cms specific attributes
    """
    request_factory = RequestFactory()
    request = request_factory.get('/')
    request.session = {}
    request.LANGUAGE_CODE = language or settings.LANGUAGE_CODE
    request.current_page = None
    request.user = AnonymousUser()
    return request


def get_text_from_placeholder(placeholder, language=None, request=None):
    """
    Returns rendered and strippet text from given placeholder
    """
    if not placeholder:
        return ''
    if not language:
        language = get_current_language()
    if not request:
        request = get_request(language)

    bits = []
    plugins = placeholder.cmsplugin_set.filter(language=language)
    for base_plugin in plugins:
        instance, plugin_type = base_plugin.get_plugin_instance()
        if instance is None:
            continue
        bits.append(instance.render_plugin(context=RequestContext(request)))
    return force_unicode(strip_tags(' '.join(bits)))


def paginate_queryset(queryset, page, do_paginate, page_size, orphans):
    """
    Paginate the queryset, if needed.

    page is a page number (int) to return or 'last' for last page.

    do_paginate is bool that determines if queryset should be paginated. If
    it is False, the page_number will always be 1, eg. no other page can be
    shown.

    page_size and orphans are values passed to Paginator class
    to do pagination.
    """
    paginator = Paginator(queryset, page_size, orphans=orphans)
    if do_paginate:
        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                raise Http404(_("Page is not 'last', "
                                "nor can it be converted to an int."))
    else:
        page_number = 1

    try:
        page = paginator.page(page_number)
        return (paginator, page, page.object_list, page.has_other_pages())
    except InvalidPage as e:
        raise Http404(_('Invalid page (%(page_number)s): %(message)s') % {
            'page_number': page_number,
            'message': str(e)
        })
