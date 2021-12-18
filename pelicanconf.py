AUTHOR = 'Iacchus Mercurius'
SITENAME = "Fancy Hats and Komputers"
SITEURL = 'https://iacchus.github.io/'
SITESUBTITLE = 'This is a blog for all things'

PATH = 'content'
STATIC_PATHS = ['static', 'images'] # this is relative to PATH

THEME = 'themes/attila'
TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

DEFAULT_DATE = 'fs'
#DEFAULT_DATE_FORMAT = '%a %d %b %Y %H:%M:%S'
DEFAULT_DATE_FORMAT = '%a %d %b %Y %H:%M:%S UTC%z'
ARTICLE_ORDER_BY = 'reversed-modified'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SHOW_FULL_ARTICLE = True

#MARKUP = ('md', 'ipynb')
MARKUP = ('md')

IPYNB_MARKUP_USE_FIRST_CELL = True

DISPLAY_PAGES_ON_MENU = True

PLUGIN_PATHS = [
    'plugins'
]

PLUGINS = [
    #'just_table',
    #'liquid_tags.youtube',
    #'liquid_tags.notebook',
    #'pelican_jupyter.markup',
    #'pelimoji',
    'pin_to_top',
    #'post_revision',
    #'render_math',
    #'rmd_reader',
    'show_source',
    # 'summary',
]

IGNORE_FILES = [".ipynb_checkpoints"]

MARKDOWN = {
    'extensions_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.footnotes': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.nl2br': {},
        'markdown.extensions.toc': {},
        'markdown.extensions.attr_list': {},
        #'pymdownx.superfences': { 'highlight_code': False },
    },
    'extensions': ['extra', 'footnotes', 'meta', 'nl2br', 'toc',
                   'attr_list']
    #'extensions': ['extra', 'footnotes', 'meta', 'nl2br', 'toc', 'attr_list',
    #     #               'pymdownx.extra', 'pymdownx.superfences'],
    #     'extensions': ['pymdownx.extra', 'pymdownx.superfences'],
    #     #'extensions': ['pymdownx'],
    #
}
#  use third-party extensions to enhance pairs markdown  language parsing, but first installation  pymdown-extensions  the module
#MATH_JAX = {
#    'message_style': None,
#}

SHOW_SOURCE_IN_SECTION = True
SHOW_SOURCE_ALL_POSTS = True
# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 22

AUTHORS_BIO = {
    "iacchus mercurius": {
        "name": "IACCHVS",
        "cover": "https://avatars2.githubusercontent.com/u/881531?v=3&u=ced26c8fd97409f69ee0237da7b87cce1790fb16&s=700",
        "image": "https://avatars2.githubusercontent.com/u/881531?v=3&u=ced26c8fd97409f69ee0237da7b87cce1790fb16&s=400",
        "website": "https://iacchus.github.io",
        "location": "cyber space",
        "bio": "My interests are in the fields of philosophy as well as arts & culture; I love music; very interested in e-learning; Also like spirituality, and humanities."
    }
}

GOOGLE_ANALYTICS = "UA-100408965-1"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True