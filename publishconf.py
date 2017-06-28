#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://yardstick17.github.io'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True
TWITTER_USERNAME = 'imYardstick17'

# Following items are often useful when publishing

DISQUS_SITENAME = "amitkushwaha"

GOOGLE_ANALYTICS = "UA-98482392-1"

MENUITEMS = (('About', SITEURL + '/pages/about-me.html'), ('Blog', SITEURL), ('Archive', SITEURL + '/archives.html'),
             ('Categories', SITEURL + '/categories.html'))

