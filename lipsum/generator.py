# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .reader import *

__all__ = [
    "generate_words",
    "generate_sentences",
    "generate_paragraphs"
]


def generate_words(count=100, filename=None, resource=None, encoding="utf-8"):
    """Generates the desired number of words from the desired source text.

    Args:
        count: The number of words to generate.
        filename: If desired, a source text file can be used to generate words. Specify the full path here.
        resource: The internal resource, within the lipsum package, from which to read text.
        encoding: The encoding to use when reading the source file.

    Returns:
        A string containing one or more sentences made up of the desired number of words.
    """
    with open_text_data(filename=filename, resource=resource, encoding=encoding) as f:
        result = read_words(f, count=count, encoding=encoding)
    return result


def generate_sentences(count=5, sentence_delimiters=set([".", "?", "!"]), filename=None, resource=None,
                       encoding="utf-8"):
    """Generates the desired number of sentences from the desired source text.

    Args:
        count: The number of sentences to generate.
        sentence_delimiters: A set containing the characters to consider as delimiters between sentences.
        filename: If desired, a source text file can be used to generate words. Specify the full path here.
        resource: The internal resource, within the lipsum package, from which to read text.
        encoding: The encoding to use when reading the source file.

    Returns:
        A string containing one or more sentences.
    """
    with open_text_data(filename=filename, resource=resource, encoding=encoding) as f:
        result = read_sentences(f, count=count, sentence_delimiters=sentence_delimiters, encoding=encoding)
    return result


def generate_paragraphs(count=3, filename=None, resource=None, encoding="utf-8"):
    """Generates the desired number of paragraphs from the desired source text.

    Args:
        count: The number of paragraphs to generate.
        filename: If desired, a source text file can be used to generate words. Specify the full path here.
        resource: The internal resource, within the lipsum package, from which to read text.
        encoding: The encoding to use when reading the source file.

    Returns:
        A string containing one or more paragraphs.
    """
    with open_text_data(filename=filename, resource=resource, encoding=encoding) as f:
        result = read_paragraphs(f, count=count, encoding=encoding)
    return result
