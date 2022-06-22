#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# processing.py

# University of Zurich
# Department of Computational Linguistics

# Author: Elina Stüssi

from typing import List, Tuple

# import os module
import os

# import sys
import sys

# the profanity word list
file = sys.argv[1]


def split_into_sentences(post_str: str) -> List[str]:
    # list with all possible endings
    endings = [".","? ","?","!",")",".. ",". ",".\"","\"","\n","…","..."]
    new = ""
    splitted= []
    # set var false
    var = False
    for index,char in enumerate(post_str):
        # if the var is true then we have two or more dots,... after each other
        if var:
            # set var false
            var = False
            # if the next char is not the same then append this part (--> that means here ends this sentence)
            if post_str[index+1] != char:
                splitted.append(new)
                # reset new
                new = ""

        # if the char is not an ending char
        elif char not in endings:
            # if it is not in this list then we don't want that char (--> it is an emoji etc)
            if char.lower() in "qwertzuiopasdfghjklyxcvbnm.-°'?^!`\"() …’\"\",“”1234567890":
                # add the char to new
                new += char
                # if it is the last char of the sentence (--> there is no ending char at the end)
                if index == (len(post_str)-1):
                    # if new is not an empty string
                    if len(new) > 0:
                        # then append new
                        splitted.append(new)
            else:
                # if the char is not in the possible chars don't add the char to new
                if index == (len(post_str)-1):
                    if len(new) > 0:
                        splitted.append(new)

        # if the char is an ending char
        elif char in endings:
            # add the char to new
            new += char
            # if it is not the last char then check if the following char is the same
            # if yes, set var true
            if index < (len(post_str)-1):
                if post_str[index+1] == char:
                    var = True
                    # add the next char to new (this is now the char at the next index)
                    new += char
            # if the next char is not the same then append new if it is not an empty string
            if not var:
                if len(new) > 0:
                    splitted.append(new)
                    new = ""

       # we don't treat the extra case where there is the combination of ". . ." because it is not necessary fot the funcionality of the program
       # now it will split after every dot but in the end the formatting will be fine :)

    # call the tokenize function with the list splitted
    tokenize(splitted)

def tokenize(sentences_str: List):
    # initiate an empty list
    tokenized_list = []
    # make a list with chars where we want to split at
    split_at = [".","?","!",")","\"","\n"," ","“","”","…"]
    for element in sentences_str:
        lischti = []
        toki = ""
        for index,char in enumerate(element):
            # if char is one of the ones above then split at that point and append toki as it is until now too the list lischti
            # then append the char
            if char in split_at:
                lischti.append(toki)
                toki = ""
                lischti.append(char)
            else:
                # add the char to toki
                toki += char
                # if char is last element of word then append it to lischti
                if index == (len(element)-1):
                    lischti.append(toki)


        del_later = []
        for index,elem in enumerate(lischti):
            # we want to delete these chars from the list 
            # if we delete it then the index changes, that's why we do that in the end
            if elem == " " or elem == "":
                del_later.append(index)

        # reverse the list such that the highest indest comes first
        # now we won't delete things we don't want to
        rev = del_later[::-1]

        for elem in rev:
            del lischti[elem]

        # we now have the tokenized list with only the elements we want to keep
        tokenized_list.append(lischti)

    # call filter_profanity function with every element and the file with the profanity words
    filter_profanity(tokenized_list,file)

def filter_profanity(tokenized: List[List[str]], filename: str) -> Tuple[List[List[str]], int]:
    # open file in read mode
    with open(file, "r", encoding="UTF-8") as profs:
        # split it and make it into a list
        prof_content = profs.read().splitlines()
        # make an empty list
        prof_list = []

        for element in tokenized:
            # variable to count how many profanity words were in the sentence
            prof_count = 0
            for index,word in enumerate(element):
                # iterate through all the bad words in the profanity list
                for bad_word in prof_content:
                    # if the bad word is in the word from the joke 
                    # --> arsed in hoarsed 
                    if bad_word in word:
                        # counter plus 1
                        prof_count += 1
                        # add instead of the word as many # as needed
                        new = len(word)*"#"
                        element[index] = new

        # the tuple is the required structure for the output
        tup = (tokenized,prof_count)

        # call the pretty_print funktion with only the list of joke and not the integer
        pretty_print(tup[0])


def pretty_print(processed: List[List[str]]) -> None:
    # empty string
    final_joke = ""
    no_space = ["?","!",")","\n","…"]
    no_space_after = ["\"","“","”"]
    for index,elem in enumerate(processed):
        #print(elem)
        # join the elements with whitespaces
        joke = " ".join(elem)

        # add the joke to the final joke
        final_joke += joke
    #print(final_joke)


    final = ""
    var = False
    space_bool = True
    for index,char in enumerate(final_joke):
        # if var is True then we don't want to have a space as the next char
        # that's why we leave the char at the next index out (because it is a whitespace because it was joined with whitespaces)
        if var:
            # add nothing to final
            final += ""
            # then we make the variable false
            var = False
        else:
            if char in no_space:
                # if it is in this list then we don't want to have a space char in front of this char
                # that's why we define final new as final without the last char
                final = final[:-1]
                final += char
                final += " "
            elif char == "“":
                final += char
                # we don't want to have a whitespace after so we set bool True
                var = True
            elif char == "”":
                final = final[:-1]
                final += char
            # if char is this symbol then there are two possible cases: start or end quotes
            elif char == "\"":
                if not space_bool:
                    # while there is a whitespace in front of this char we want to delelte the whitespaces
                    while final[-1] == " ": 
                        final = final[:-1]
                    # then we add char and a whitespace
                    final += char
                    final += " "
                    # set bool true
                    space_bool = True
                else:
                    # if it is the end of the sentence then we want a whitespace after it
                    # set bool var true
                    var = True
                    final += char
                    space_bool = False
            elif char == ".":
                # deltete whitespaces in front of dot
                while final[-1] == " ": 
                    final = final[:-1]
                final += char
                # if the index is not the last of the sentence and the next char is not a whitespace then we want to add one
                # if there already is a space then we don't add another
                if index < (len(final_joke)-1) and final_joke[index+1] != " " :
                    final += " "


            else:
                final += char


    print(final)

    return final

if __name__ == '__main__':
    split_into_sentences("Vampires. . . sure are a pain in the neck!")

