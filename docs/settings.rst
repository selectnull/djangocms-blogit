########
Settings
########


====
Info
====

Thease settings are used to render the proper values in feeds:

.. code:: python

    BLOGIT_TITLE = 'Blogit'
    BLOGIT_DESCRIPTION = 'This is a blog about everything'


=====
Feeds
=====

Feeds can be accessed on ``/<BLOGIT_FEED_URL>/rss/`` and
``/<BLOGIT_FEED_URL>/atom/`` by default. Update feeds using thease settings:

.. code:: python

    BLOGIT_RSS_FEED = True
    BLOGIT_ATOM_FEED = True
    BLOGIT_FEED_LIMIT = 100
    BLOGIT_FEED_ITEM_AUTHOR_NAME = None  # When none displays author info
    BLOGIT_FEED_ITEM_AUTHOR_EMAIL = None  # When none displays author info
    BLOGIT_FEED_ITEM_DESCRIPTION_FULL = False


==========
Pagination
==========

Pagination per page:

.. code:: python

    BLOGIT_POSTS_PER_PAGE = 5

========
Post url
========

By default post detail url is ``/<post_slug>/``. If you want to have a dated
url like this ``/<year>/<month>/<day>/<post_slug>/``, change this setting:

.. code:: python

    BLOGIT_POST_DETAIL_DATE_URL = False

=======
Plugins
=======

With default configuration, the index page of the app (as configured by AppHook)
displays a list of posts and can not be used with standard CMS plugins.  If you
want, you can disable that view and create your own list page with ``Post List``
plugin. To disable default list view, you need to do two things:

1) In your ``settings.py``, define:

.. code:: python

    BLOGIT_USE_BUILTIN_LIST_VIEW = False

2) Create your own ``blogit/post_list.html`` template and render your placeholders there.

.. code:: django

    {% placeholder "content" %}

That setting is needed only if you want to build your own page for blog index
with custom layout.  ``Post List`` plugin can be used no matter what
``BLOGIT_USE_BUILTIN_LIST_VIEW`` setting is on any other page (not the page
configured by AppHook).

``Post List`` plugin can be configured to lists post filtered by author, tags
or categories (those can be combined). It can also be configured to display only
certain number of posts, and to display paginator or not (with orphans).

Examples of use:

* on ``/blog/`` page list all posts with pagination
* on website homepage, lists 3 latest posts without pagination
* on user's profile page (outside of ``blogit`` app),
  list latest posts by that user

For different cases, you can create different templates to be used with plugin.
Define ``BLOGIT_POST_LIST_TEMPLATES`` like this:

.. code:: python

    BLOGIT_POST_LIST_TEMPLATES = (
        ('blogit/plugins/post_list.html', 'Default'),
        ('blogit/plugins/homepage.html', 'Latest posts on homepage'),
        ...
    )

There are two more plugins available: ``Category List`` and ``Tag List``. Those
can be used anywhere, even with default list view. They have no options.
