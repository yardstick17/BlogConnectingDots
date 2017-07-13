#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Amit Kushwaha'
SITENAME = 'Connecting Dots'
SITEURL = 'http://localhost:8000'

PATH = 'content'

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
# RELATIVE_URLS = True
TWITTER_USERNAME = 'imYardstick17'

THEME = 'pelican-blue'
# THEME = 'bootlex'
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/yardstick17'),
          ('github', 'https://github.com/yardstick17'),
          ('twitter', 'https://twitter.com/imYardstick17'),
          )

SIDEBAR_DIGEST = 'AI | NLP | DEEP LEARNING'

FAVICON = 'url-to-favicon'

DISPLAY_PAGES_ON_MENU = True

MENUITEMS = (('About Me', SITEURL + '/pages/about-me.html'), ('Blog', SITEURL), ('Archive', SITEURL + '/archives.html'),
             ('Categories', SITEURL + '/categories.html'))

DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_CATEGORY = 'misc'

DISQUS_SITENAME = "amitkushwaha"
# HEADER_IMAGE = FAVICON
