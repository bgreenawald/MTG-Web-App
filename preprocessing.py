#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Perform the necesary text preprocessing on the input files.
"""

import re

def preprocessing(text):
    """ Take in a complete text and preprocess it.

    Args:
        text (string): A collection of statements, one per line, to be used
            in the program.

    Returns:
        (string): A collection of statements, one per line, after subject
            to the preprocessing pipeline.

    """

    # Regular expression to consolidate paragraphs into a single line
    single_line = re.compile("\n(?!\n)")

    # Core regex's needed to process the data
    remove_non_alphabetic = re.compile("[^a-zA-Z \n]")
    remove_multiple_newlines = re.compile("\n[\n]+")
    remove_multiple_spaces = re.compile(" [ ]+")

    # Additional useful regex's
    remove_links = re.compile("http[^ ]+")

    # Run the text through the core regular expressions
    text = re.sub(pattern=single_line, string=text, repl=" ")
    text = re.sub(pattern=remove_non_alphabetic, string=text, repl=" ")
    text = re.sub(pattern=remove_multiple_newlines, string=text, repl=" ")
    text = re.sub(pattern=remove_multiple_spaces, string=text, repl=" ")

def core_regex(text):
    """
    Run the text through a series of core regular
    expressions needed to preprocess the data.

    Args:
        text (string): The unprocessed text.

    Returns:
        (string): The processed text.