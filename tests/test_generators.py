# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from lipsum import *


class TestLipsumGenerators(unittest.TestCase):

    def test_generate_words(self):
        for i in range(5):
            desired_word_count = rnd(100, 500)
            print("Attempting to generate %d words..." % desired_word_count)
            self.assertEqual(desired_word_count, count_words(generate_words(desired_word_count)))

    def test_generate_sentences(self):
        for i in range(5):
            desired_sentence_count = rnd(2, 10)
            print("Attempting to generate %d sentences..." % desired_sentence_count)
            self.assertEqual(desired_sentence_count, count_sentences(generate_sentences(desired_sentence_count)))

    def test_generate_paragraphs(self):
        for i in range(5):
            desired_paragraph_count = rnd(2, 7)
            print("Attempting to generate %d paragraphs..." % desired_paragraph_count)
            self.assertEqual(desired_paragraph_count, count_paragraphs(generate_paragraphs(desired_paragraph_count)))
