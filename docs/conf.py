# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Reconcycle'
copyright = '2023, Reconcycle.eu'
author = 'Reconcycle'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    #'sphinx.ext.duration',
    #'sphinx.ext.doctest',
    #'sphinx.ext.autodoc',
    #'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
    'sphinx_design',
    'sphinx_copybutton',
    'sphinx.ext.extlinks',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_static_path = ['_static']
html_logo = "figures_main_page/reconcycle-transparent.png"
#html_theme = 'sphinx_rtd_theme'
#html_theme_options = {
#    'logo_only': True,
#    'display_version': False,
#}
html_baseurl = 'https://reconcycle.github.io'

html_theme = 'furo'
html_theme_options = {
    "source_repository": "https://github.com/reconcycle/reconcycle.github.io/",
    "source_branch": "main",
    "source_directory": "docs/",
}
master_doc = 'index'


# -- Options for EPUB output
epub_show_urls = 'footnote'

## Icon
html_favicon = "favicon.ico"