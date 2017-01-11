# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import pkg_resources
import os
import os.path
from io import open

from .utils import rnd

__all__ = [
    "open_text_data",
    "wrapped_readline",
    "seek_to_random_paragraph",
    "read_words",
    "read_sentences",
    "read_paragraphs"
]


def prep_string(s, sentence_delimiters=[".", "?", "!"]):
    """Prepares and cleans up the given string."""
    if len(s) > 1:
        # replace any double-spaces with single ones
        result = s.strip().replace("  ", " ")
        # capitalise the first letter of the string
        result = ("%s" % result[0]).upper() + result[1:]
        # ensure a sentence delimiter at the end of the string
        if result[-1] not in sentence_delimiters:
            result = result[:-1] + sentence_delimiters[rnd(len(sentence_delimiters))]

        return result

    # unmodified
    return s


def open_text_data(filename=None, resource=None, random_para=True, encoding="utf-8"):
    """Opens the given file or resource for reading as a lipsum text data file.

    Args:
        filename: The full path to the file to open (optional).
        resource: The resource, within this lipsum package, to open (optional).
        random_para: Open the file at a random paragraph? (default: True).
        encoding: The encoding to use when reading from the file.

    Returns:
        A file descriptor that can be used for reading the contents of the file.
    """
    if filename is None and resource is None:
        resource = "data/definibus.txt"

    if filename is None:
        filename = pkg_resources.resource_filename("lipsum", resource)

    file_size = os.path.getsize(filename)
    if file_size < 102400:
        raise IOError("Input file must be at least 100kB in size, but is %dkB" % file_size)

    f = open(filename, "rb")
    if random_para:
        seek_to_random_paragraph(f, file_size, encoding=encoding)

    return f


def wrapped_readline(f, encoding="utf-8"):
    """Attempts to read a line of text from the given file and wraps back around to the beginning of
    the file when the end of the file has been reached.
    """
    line = f.readline(1024).decode(encoding)
    # EOF?
    if len(line) == 0:
        f.seek(0, os.SEEK_SET)
        # hopefully we get a line now
        line = f.readline(1024).decode(encoding)
    return line


def seek_to_random_paragraph(f, file_size, encoding="utf-8"):
    """Seeks in the file to a random paragraph."""
    # seek to a random byte position in the file
    f.seek(rnd(file_size), os.SEEK_SET)

    # read lines until we find the beginning of the next paragraph
    done = False
    last_line = ""
    while not done:
        line = wrapped_readline(f, encoding=encoding)
        # if we've encountered a line of text after one or more newlines, consider it the beginning of a new
        # paragraph
        if last_line == "\n" and len(line) > 1:
            # seek backwards to the beginning of the line
            f.seek(-len(line), os.SEEK_CUR)
            done = True

        last_line = line


def read_words(f, count=100, encoding="utf-8"):
    """Reads the given number of words from the specified open file."""
    result = []
    while len(result) < count:
        line = wrapped_readline(f, encoding=encoding).strip()
        words = [w.strip() for w in line.split(" ")]
        # remove empty words
        words = [w for w in words if len(w) > 0]
        if len(result) + len(words) > count:
            result.extend(words[:count-len(result)])
        else:
            result.extend(words)

    return prep_string(" ".join(result))


def read_sentences(f, count=5, sentence_delimiters=set([".", "?", "!"]), encoding="utf-8"):
    """Reads the given number of sentences from the specified open file."""
    result = []
    cur_sentence = ""
    while len(result) < count:
        line = wrapped_readline(f, encoding=encoding).strip()
        if len(line) > 0:
            for c in line:
                cur_sentence += c
                if c in sentence_delimiters:
                    result.append(prep_string(cur_sentence))
                    cur_sentence = ""
                    if len(result) >= count:
                        break

    return " ".join(result)


def read_paragraphs(f, count=3, encoding="utf-8"):
    """Reads the given number of paragraphs of text from the specified open file."""
    result = []
    cur_paragraph = ""
    last_line = ""
    while len(result) < count:
        line = wrapped_readline(f, encoding=encoding)
        # if we've hit the end of a paragraph
        if len(last_line) > 1 and line == "\n":
            result.append(prep_string(cur_paragraph))
            cur_paragraph = ""
        elif len(line) > 1:
            # if we're still building the current paragraph
            cur_paragraph += line

        last_line = line

    return "\n\n".join(result)
