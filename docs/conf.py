# Configuration file for the Sphinx documentation builder.
# Week 11: Quantum Mechanics Simulation Manual

import os
import sys

# -- Project information -------------------------------------------------------
project = 'Week 11: 양자역학 시뮬레이션'
copyright = '2026, Computational Physics Course'
author = 'AI & ML Course'
release = '1.0'

# -- General configuration -----------------------------------------------------
extensions = [
    'sphinx.ext.mathjax',       # LaTeX 수식 렌더링
    'sphinx.ext.viewcode',      # 소스코드 링크
    'sphinx.ext.autodoc',       # 자동 문서화
    'sphinx.ext.napoleon',      # Google/NumPy docstring
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
language = 'ko'

# -- Options for HTML output ---------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_title = 'Week 11: 양자역학 시뮬레이션 매뉴얼'

html_theme_options = {
    'navigation_depth': 4,
    'titles_only': False,
    'collapse_navigation': False,
    'sticky_navigation': True,
}

# -- MathJax configuration -----------------------------------------------------
mathjax3_config = {
    'tex': {
        'inlineMath': [['$', '$'], ['\\(', '\\)']],
        'displayMath': [['$$', '$$'], ['\\[', '\\]']],
    }
}

# -- Options for LaTeX output (PDF) --------------------------------------------
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'preamble': r'''
\usepackage{kotex}
\usepackage{amsmath}
\usepackage{amssymb}
''',
}
