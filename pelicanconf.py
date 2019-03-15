#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os


AUTHOR = 'Amit Kushwaha'
SITENAME = 'Connecting Dots'
SITEURL = 'http://localhost:8000'

PATH = 'content'

# STATIC_PATHS = ['images', 'pdfs', 'downloads']
# STATIC_PATHS = ['blog', 'downloads']
# ARTICLE_PATHS = ['blog']
# ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
# ARTICLE_URL = '{date:%Y}/{slug}.html'

TIMEZONE = 'Asia/Calcutta'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
TWITTER_USERNAME = 'imYardstick17'

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

IGNORE_FILES = [".ipynb_checkpoints"]

# if you create jupyter files in the content dir, snapshots are saved with the same
# metadata. These need to be ignored.

EFFECTIVE_THEME = 'aboutwilson'
EFFECTIVE_THEME = 'elegant'
THEME = os.path.expanduser('~/pelican-themes/{}'.format(EFFECTIVE_THEME))
# THEME = 'bootlex'
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/yardstick17'),
          ('github', 'https://github.com/yardstick17'),
          ('twitter', 'https://twitter.com/imYardstick17'),
          )

SIDEBAR_DIGEST = 'AI | NLP | DEEP LEARNING'

FAVICON = SITEURL + '/images/favicon.ico'

DISPLAY_PAGES_ON_MENU = True

MENUITEMS = (('About Me', 'pages/about-me.html'), ('Blog', ''), ('Archive', 'archives.html'),
             ('Categories', 'categories.html'))

DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_CATEGORY = 'misc'

DISQUS_SITENAME = "amitkushwaha"
# HEADER_IMAGE = FAVICON
# MENUITEMS = (('Blog', SITEURL),)
