#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Perform the necesary text preprocessing on the input files."""

import re


def preprocessing(text):
    """
    Take in a complete text and preprocess it.

    Args:
        text (string): A collection of statements, one per line, to be used
            in the program.

    Returns:
        (string): A collection of statements, one per line, after subject
            to the preprocessing pipeline.

    """
    # Run the text through both sets of regular expressions
    text = core_regex(text)
    text = additional_regex(text)

    # Run through two final cleanup expressions.
    text = text.replace("\n", "ENDLINE\n")
    remove_multiple_spaces = re.compile(" [ ]+")
    text = re.sub(pattern=remove_multiple_spaces, string=text, repl=" ")

    return text


def core_regex(text):
    """
    Run the text through core regular expressions.

    Args:
        text (string): The unprocessed text.

    Returns:
        (string): The processed text.

    """
    # Regular expression to consolidate paragraphs into a single line
    single_line = re.compile("\n(?!\n)")

    # Core regex's needed to process the data
    remove_non_alphabetic = re.compile("[^a-zA-Z \n]")
    remove_multiple_newlines = re.compile("\n[\n]+")

    # Run the text through the core regular expressions
    text = re.sub(pattern=single_line, string=text, repl=" ")
    text = re.sub(pattern=remove_non_alphabetic, string=text, repl=" ")
    text = re.sub(pattern=remove_multiple_newlines, string=text, repl=" ")

    return text


def additional_regex(text):
    """
    Run the text through additional helpful regular expressions.

    Args:
        text (string): The text that has already gone through the core regular
            expressions.

    Returns:
        (string): The additionally processed text.

    """
    # Define the additional regular expressions
    remove_http = re.compile("http[^ ]+")

    # Run the text through the regular expressions.
    text = re.sub(pattern=remove_http, string=text, repl=" ")

    return text
