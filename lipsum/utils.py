# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

__all__ = [
    "count_words",
    "count_sentences",
    "count_paragraphs",
    "rnd"
]


def count_words(s):
    """Counts the number of words in the given string."""
    cs = " ".join([p.strip() for p in s.split("\n")])
    return len(cs.split(" "))


def count_sentences(s, sentence_delimiters=set([".", "!", "?"])):
    """Counts the number of sentences in the given string."""
    cs = " ".join([p.strip() for p in s.split("\n")])
    count = 0
    for c in cs:
        if c in sentence_delimiters:
            count += 1
    return count


def count_paragraphs(s):
    """Counts the number of paragraphs in the given string."""
    last_line = ""
    count = 0
    for line in s.split("\n"):
        if len(line) > 0 and (len(last_line) == 0 or last_line == "\n"):
            count += 1
        last_line = line
    return count


def rnd(*args):
    """Securely generates a random number according to the given constraints. If one parameter is given, it is
    assumed that an integer between 0 (inclusive) and max_val (exclusive) is to be generated. If two parameters are
    given, it is assumed that an integer between min_val (inclusive) and max_val (exclusive) is to be generated.
    """
    if len(args) == 1:
        min_val, max_val = 0, args[0]
    elif len(args) > 1:
        min_val, max_val = args[0], args[1]
    else:
        raise ValueError("Missing argument(s) for rnd()")

    temp_max_val = max_val - min_val

    bits_required = len(bin(temp_max_val))-2
    bytes_required = (bits_required // 8) + 1
    rndval = 0
    cur_bitshift = (bytes_required - 1) * 8
    for b in bytearray(os.urandom(bytes_required)):
        rndval += b << cur_bitshift
        cur_bitshift -= 8

    return min_val + (rndval % temp_max_val)
