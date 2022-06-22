#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# test_processing.py

# University of Zurich
# Department of Computational Linguistics

# Authors: Elina Stüssi


# Test Units for dad_jokes Analyzer Engine
# Module for functional and non functional testing of dad_jokes_processor module

# Import Statements
from unittest import TestCase, main
import processing
from os import path


class LpTest(TestCase):

    # tests for split into sentences (Task1)

    def test_output_split_into_sentences_function(self):
        dad_jokes = "Want to hear a construction joke?\nI'm working on it."
        result = processing.split_into_sentences(dad_jokes)
        self.assertIsInstance(result, list, "Required type of output is list")
        #TODO: 2 own test assertions

    # # checks if the program does not crash when the wrong type is entered
    # def test_integer(self):
    #     dad_jokes = 7
    #     result = processing.split_into_sentences(dad_jokes)
    #     self.assertEqual(result,"Sorry, we cannot fullfill your wishes. Please enter a string.")

    # checks if the solution is not none -> means it does at least something
    def test_not_none(self):
        dad_jokes = "Want to hear a construction joke?\nI'm working on it."
        result = processing.split_into_sentences(dad_jokes)
        self.assertIsNotNone(result)

    # tests if the newline is in the result or if it has been removed
    def test_newline_is_in(self):
        dad_jokes = "Want to hear a construction joke?\nI'm working on it."
        result = processing.split_into_sentences(dad_jokes)
        self.assertIn("\n", result)

    # test if the function removes emojis anywhere in the sentence
    def test_emojis(self):
        dad_jokes = "☝Want to hear a construction joke?😄\nI'm working on it.😄☝"
        result = processing.split_into_sentences(dad_jokes)
        self.assertEqual(result, ["Want to hear a construction joke?","\n","I'm working on it."])



    # tests for tokenization (Task2)

    def test_output_tokenize_function(self):
        split_dad_jokes = ["Want to hear a construction joke?", "\n", "I'm working on it."]
        result = processing.tokenize(split_dad_jokes)
        target = [["Want", "to", "hear", "a", "construction", "joke", "?"], ["\n"], ["I'm", "working", "on", "it", "."]]
        self.assertEqual(result, target)

    # test to check if it splits at the correct place
    def test_tokenize_len(self):
        split_dad_jokes = ["Want to hear a construction joke?", "\n", "I'm working on it."]
        result = processing.tokenize(split_dad_jokes)
        target = [["Want", "to", "hear", "a", "construction", "joke", "?"], ["\n"], ["I'm", "working", "on", "it", "."]]
        dad_jokes = "Want to hear a construction joke?\nI'm working on it."
        index_sent = dad_jokes.index(" ")
        # the lenght of the first part of the splittet sentence is equal to the index of the first whitespace because the index starts at 0
        self.assertEqual(len(target[0][0]),index_sent)

    # test if there is a list in a list as output
    def test_type_tok(self):
        split_dad_jokes = ["Want to hear a construction joke?", "\n", "I'm working on it."]
        result = processing.tokenize(split_dad_jokes)
        target = [["Want", "to", "hear", "a", "construction", "joke", "?"], ["\n"], ["I'm", "working", "on", "it", "."]]
        for elem in result:
            type_tar = type(elem)
        self.assertEqual(list, type_tar, "Required type of output is list in a list")



    # tests for profanity filter (Task3)

    def test_output_filter_profanity_function(self):
        tokenized_dad_jokes = [["Want", "to", "fuck", "a", "construction", "joke", "?"], ["\n"], ["I'm", "working", "on", "it", "."]]
        result = processing.filter_profanity(tokenized_dad_jokes,"profanities.txt")
        target = ([['Want', 'to', '####', 'a', 'construction', 'joke', '?'], ['\n'], ["I'm", 'working', 'on', 'it', '.']], 1)
        self.assertEqual(target,result)

    # tests if not every word is being replaced by #
    def test_not_equal(self):
        tokenized_dad_jokes = [["Want", "to", "fuck", "a", "construction", "joke", "?"], ["\n"], ["I'm", "working", "on", "it", "."]]
        result = processing.filter_profanity(tokenized_dad_jokes,"profanities.txt")
        target = ([['####', '##', '####' '#', '############','####', '#'], ['#'], ["###", '#######', '##', '##', '#']], 13)
        self.assertNotEqual(target,result)

    # test to check if the integer in the tuple is correct
    def test_int_tup(self):
        tokenized_dad_jokes = [["Want", "to", "fuck", "a", "hoarse", "joke", "?"], ["\n"], ["I'm", "working", "on", "it", "."]]
        result = processing.filter_profanity(tokenized_dad_jokes,"profanities.txt")
        target = ([["Want", "to", "####", "a", "######", "joke", "?"], ["\n"], ["I'm", "working", "on", "it", "."]], 2)
        self.assertEqual(result[1], target[1])

    # tests if type is tuple
    def test_for_tuple(self):
        tokenized_dad_jokes = [["Want", "to", "fuck", "a", "construction", "joke", "?"], ["\n"], ["I'm", "working", "on", "it", "."]]
        result = processing.filter_profanity(tokenized_dad_jokes,"profanities.txt")
        target = ([["Want", "to", "####", "a", "construction", "joke", "?"], ["\n"], ["I'm", "working", "on", "it", "."]], 1)
        self.assertIsInstance(result, tuple, "Required type of output is tuple")
      

