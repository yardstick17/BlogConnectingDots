#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://amitk.org'
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True
TWITTER_USERNAME = 'imYardstick17'

# Following items are often useful when publishing

DISQUS_SITENAME = "amitkushwaha"

GOOGLE_ANALYTICS = "UA-98482392-1"
FAVICON = SITEURL + '/images/favicon.ico'
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

IGNORE_FILES = [".ipynb_checkpoints"]

MENUITEMS = (('About Me', 'pages/about-me.html'), ('Blog', ''), ('Archive', 'archives.html'),
             ('Categories', 'categories.html'))
