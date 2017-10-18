#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITENAME = "Improtech 2017"
SITEURL = 'http://ikparisphilly.ircam.fr'
# AUTHOR = 'Guillaume Pellerin'
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = '/srv/lib/pelican-themes/pelican-bootstrap3'


BOOTSTRAP_THEME = 'united'
#BOOTSTRAP_THEME = 'yeti'
# CUSTOM_CSS = 'themes/bootswatch/slate/slate/bootstrap.css'

PATH = '/var/in'
OUTPUT_PATH = '/var/out'
STATIC_PATHS = ['doc', 'images', 'extra']

#NEST_HEADER_IMAGE = '/images/header.png'
#NEST_HEADER_LOGO = '/images/logo.png'
#HEADER_IMAGE = "header.png"

BANNER = '/images/IKPoster_Banner.png'
BANNER_SUBTITLE = ''
BANNER_ALL_PAGES = True

#SIDEBAR_IMAGES_HEADER = 'IKGraphicID.png'
#SIDEBAR_IMAGES = ["/images/omax.png","/images/omax.png"]

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

SUMMARY_MAX_LENGTH = 127
SLUGIFY_SOURCE = 'title'
# DEFAULT_PAGINATION = 5


# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Ircam', 'http://www.ircam.fr'),
          )

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/Ircam/'),
          ('GitHub', 'https://github.com/Ircam-RnD/'),
          ('FaceBook', 'https://www.facebook.com/iIRCAM/'),
          ('Youtube', 'https://www.youtube.com/user/Ircam75'),
          ('DailyMotion', 'https://www.dailymotion.com/RepMus'),
          ('Vimeo', 'https://vimeo.com/user15042869'),
          )

#DISQUS_SITENAME='ismir2018'
GITHUB_USER = ''
TWITTER_CARDS = False
TWITTER_USERNAME = 'ircam'
TWITTER_WIDGET_ID = '516222825451888640'

PLUGIN_PATHS = ['/srv/lib/pelican-plugins']
PLUGINS = ['assets', 'i18n_subsites', 'jinja2content', 'sitemap', 'gallery',
        #     'neighbors',
        #    'liquid_tags.img', 'liquid_tags.video',
        #    'liquid_tags.youtube', 'liquid_tags.vimeo',
        #    'liquid_tags.include_code',
        #    'liquid_tags.notebook',
           ]

SITEMAP = {

    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Content licensing: CC-BY
CC_LICENSE = "CC-BY"

# GOOGLE_ANALYTICS = 'UA-6573030-16'

GALLERY_PATH = '/var/in/img/gallery/'

PELICANGIT_SOURCE_REPO=PATH
PELICANGIT_SOURCE_REMOTE="origin"
PELICANGIT_SOURCE_BRANCH="master"

PELICANGIT_DEPLOY_REPO=OUTPUT_PATH
PELICANGIT_DEPLOY_REMOTE="origin"
PELICANGIT_DEPLOY_BRANCH="master"
PELICANGIT_DEPLOY_IS_LOCAL_DIR = True

PELICANGIT_USER = "root"
PELICANGIT_WHITELISTED_FILES = [
    "README.md"
]

PELICANGIT_PORT=8888

#MARKDOWN = {'extensions': ['markdown.extensions.meta',]}

MARKDOWN = {
    'extensions': ['markdown.extensions.meta',],
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
        },
        'markdown.extensions.extra': {},
        # optionally, more extensions,
        # e.g. markdown.extensions.meta
    },
    'output_format': 'html5',
}


JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n',]}

I18N_SUBSITES = {
    'fr': {
        'SITENAME': 'Improtech 2017',
        }
    }

DISPLAY_PAGES_ON_MENU = True

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'},
    'extra/custom.js': {'path': 'static/js/custom.js'}
}

SHOW_DATE_MODIFIED = False


HIDE_SIDEBAR = False
BOOTSTRAP_NAVBAR_INVERSE = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_CATEGORIES_ON_MENU = False

