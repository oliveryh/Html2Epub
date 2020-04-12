#!usr/bin/python3
# -*- coding: utf-8 -*-

# Included modules

# Third party modules
from bs4 import BeautifulSoup

# Local modules

def style(input_string):
    """
    Adds the stylesheet to the chapters head
    """

    try:
        assert isinstance(input_string, str)
    except AssertionError:
        raise TypeError
    root = BeautifulSoup(input_string, 'html.parser')
    head = root.head
    style_tag = root.new_tag("link", href="styles/stylesheet.css", rel="stylesheet", type="text/css")
    head.append(style_tag)
    return root.prettify()