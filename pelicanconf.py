AUTHOR = 'Iacchus Mercurius'
SITENAME = "Fancy Hats and Komputers"
SITEURL = 'https://iacchus.github.io/'
SITESUBTITLE = 'This is a blog for all things'

PATH = 'content'
STATIC_PATHS = ['static', 'images'] # this is relative to PATH

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SHOW_FULL_ARTICLE = True

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
# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 22

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True