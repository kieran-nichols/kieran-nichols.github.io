#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'kieran-nichols'
SITENAME = 'Kieran Nichols'
SITEURL = 'https://www.kieran-nichols.com'

PATH = 'content'

OUTPUT_PATH = 'docs/'

TIMEZONE = 'US/Central'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISPLAY_CATEGORIES_ON_MENU = True

THEME = 'themes/Bulrush'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets']

import bulrush

THEME = bulrush.PATH
JINJA_ENVIRONMENT = bulrush.ENVIRONMENT
JINJA_FILTERS = bulrush.FILTERS

SOCIAL = (
    ('Email', 'knichols4@wisc.edu'),
    ("Github", "https://github.com/kieran-nichols/"),
    ("LinkedIn", "https://www.linkedin.com/in/kieran-nichols-24134479/")
)

#MENUITEMS = (
  #('Resume','resume'),
  #('Portfolio','portfolio'),
  #('About Me','about-me'),
#)

#DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True