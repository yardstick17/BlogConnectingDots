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

THEME = 'pelican-blue'
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/yardstick17'),
          ('github', 'https://github.com/yardstick17'),
          ('twitter', 'https://twitter.com/iamYardstick17'),
          )

SIDEBAR_DIGEST = 'AI | NLP | DEEP LEARNING'

FAVICON = 'https://b.zmtcdn.com/images/logo/zomato_logo.svg'

DISPLAY_PAGES_ON_MENU = True

TWITTER_USERNAME = 'iamYardstick17'

MENUITEMS = (('About', SITEURL + '/pages/about-me.html'), ('Blog', SITEURL),)

DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_CATEGORY = 'misc'

DISQUS_SITENAME = "amitkushwaha"
HEADER_IMAGE = FAVICON
