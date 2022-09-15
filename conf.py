# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'NDN Packet Format Specification'
copyright = '2013-2022, Named Data Networking Project'

# The short X.Y version.
version = '0.3'

# The full version, including alpha/beta/rc tags.
release = '0.3'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

needs_sphinx = '4.0'
extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_title = '{} {}'.format(project, version)
html_logo = '_static/ndn-logo.svg'
html_copy_source = False
html_show_sourcelink = False

html_theme_options = {
    'light_css_variables': {
        'color-brand-primary': '#fd7800',
        'color-brand-content': '#fd7800',
    },
    'dark_css_variables': {
        'color-brand-primary': '#fd7800',
        'color-brand-content': '#fd7800',
    },
}

# Use ABNF syntax highlighting by default for code blocks.
highlight_language = 'abnf'

pygments_dark_style = 'material'
