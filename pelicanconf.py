#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Anil Gomes & Colin McLear'
SITENAME = u'Kant on Perception & Cognition'
SITEURL = 'http://ox-kant.colinmclear.net'
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
PATH = 'content'
FAVICON = 'images/favicon.ico'
READERS = {'html': None}

# THEME SETTINGS ########
THEME = 'pelican-bootstrap3'
BOOTSTRAP_THEME='simplex'
BOOTSTRAP_NAVBAR_INVERSE = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_PAGES_ON_MENU = False
NEWEST_FIRST_ARCHIVES = False
MENUITEMS = (
    ('Schedule', '/schedule'),
    ('Readings', '/readings'),
    ('Resources', '/resources'),
    ('Contact', '/contact'),
    # ('Syllabus', '/syllabus'),
    # ('Tags', '/tags.html'),
    # ('Home', '/'),
    # ('Category1', 'category/category1.html'),
    # ('Category2', 'category/category2.html'),
)
THEME_STATIC_DIR = 'theme'
# Turn on Typogrify
TYPOGRIFY = True
CC_LICENSE = "CC-BY-NC-SA"
ARTICLE_PATHS = ['readings']
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
INDEX_SAVE_AS = 'readings/index.html'
INDEX_URL = 'readings/'
CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['images', 'readings', 'extra', 'slides', 'materials']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'extra/custom.css': {'path': 'static/custom.css'}}
DIRECT_TEMPLATES = ('index', 'tags', 'authors', 'archives', 'search')

# Plugins ##########
PLUGIN_PATHS = ['/Users/Roambot/bin/pelican-plugins']
PLUGINS = ['org_pandoc_reader', 'assets', 'tipue_search', 'tag_cloud', 'neighbors', 'extract_toc', 'encrypt_content']

ORG_PANDOC_ARGS = [
    '--filter=/usr/local/bin/pandoc-citeproc',
    '--base-header-level=2',
    '--bibliography=/Users/Roambot/Dropbox/Work/Master.bib',
    '--mathjax',
    '--toc',
    '--toc-depth=5',
  ]

ENCRYPT_CONTENT = {
    'title_prefix': '[Encrypted]',
    'summary': 'This content is encrypted. Please enter the password'
}
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Tags

TAG_CLOUD = True
DISPLAY_TAGS_ON_SIDEBAR= True
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = 'random'


# Blogroll
# LINKS = (
#         ('Blackboard', 'https://my.unl.edu/webapps/portal/frameset.jsp'),
#         ('UNL Philosophy', 'http://www.unl.edu/philosophy/'))

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
