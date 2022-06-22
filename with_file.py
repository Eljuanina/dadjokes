#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# processing.py

# University of Zurich
# Department of Computational Linguistics

# Authors: # Elina Stüssi


from typing import List, Tuple

# import os module
import os
# import the sys module
import sys

import re

# file with dadjokes
file = sys.argv[1]

# the profanity list
file2 = sys.argv[2]


def split_into_sentences(post_str: str) -> List[str]:
    # open the file with the dadjokes in readmode as jokes
    with open(post_str, "r", encoding="UTF-8") as jokes:
        # read the text and split it at end of lines
        # lines is a list
        lines = jokes.read().splitlines()
        # create new list
        list_cleaned = []
        # list with possible endings
        # endings = [".","? ","?","!",")",".. ",". ",".\"","\"","\n","…","..."]
        # iterate through the lines
        for index,element in enumerate(lines):
            # initialise empty string for each line in lines
            cleaned = ""
            # iterate over the characters
            for char in element:
                # only apppend the character to cleaned if it is one of these
                #if char.isascii() wpuld be more beautiful but it does not recognize "’" then so I go with the list of possible chars
                if char.lower() in "qwertzuiopasdfghjklyxcvbnm.-°'?^!`\"() …’\"\",“”1234567890":
                    cleaned += char
            # say element (the line) is now the cleaned version of original element
            element = cleaned

            # go through line and chekc if there is a "?"
            if "?" in element:
                if "? " in element:
                    splitted = element.split("? ")
                # split at "?"
                else:
                    splitted = element.split("?")
                # because it was splitted at "?", the "?" is no longer there and we have to append it anew
                # but we don't want the whitespace
                splitted[0] += "?"


                # if it is the case that there is a sentence in parentheses in element we have to split there too
                for elem in splitted:
                    if ")" in element:
                        # split at ) plut whitespace to eliminate the whitespace
                        splittie = elem.split(") ")
                        splittie[0] += ")"

                        splitted = [splitted[0],splittie[0],splittie[-1]]

                if not ")" in element:
                    for elem in splitted:
                        if ".. " in elem:
                            # split at the doppel dot
                            spl = elem.split(".. ")
                            spl[0] += ".."

                            # # split one is a list containing both elements of spl
                            # split1 = [spl[0],spl[1]]

                            for ele in splitted[1]:
                                #print(ele)
                                if "nn" in ele:
                                    splittie = ele.split("nn")
                            
                            # if there would have been two newline chars then add them later
                            splitted = [spl[0],spl[1],"\n","\n",splitted[1][2:]]



                list_cleaned.append(splitted)


            elif "..." in element:
                splitted = element.split("... ")
                splitted[0] += "..."

                list_cleaned.append(splitted)



            # we don't have to check for the case of "!" because it only comes at the end of the lines in our examples and the sentence will always be covered by one of the other cases
            
            # elif "!" in element:
            #     splitted = element.split("!")
            #     splitted[0] += "!"
            #     # because the "!" is at the end of line in these examples and then there is nothing in splitted[-1], so we can delete it
            #     del splitted[-1]
            #     list_cleaned.append(splitted)

        
            # check if there is . . . in line. if yes, then we don't have to split with our examples
            elif ". . ." in element:
                ele = []
                for el in element:
                    ele.append(el)
                joined = "".join(ele)
                joinie = []
                joinie.append(joined)
                list_cleaned.append(joinie)

            # look it there is a dot followed by a " is in the line
            elif ".\"" in element:
                add = False
                # if the line ends with that we have to append make add = True
                if element.endswith(".\""):
                    add = True
                splitted = element.split(".\"")
                # that means there are at least 3 parts --> we have splitted multiple times at ."
                # append not ." after the fist split
                if len(splitted) >2:
                    splitted[0] += ".\""
                # because the "\."" is at the end of line in these examples and then there is nothing in splitted[-1], so we can delete it
                del splitted[-1]
                # because it was at the end we have to append it again there
                if add:
                    splitted[-1] += ".\""
                list_cleaned.append(splitted)

            elif "…" in element:
                splitted = element.split("… ")
                splitted[0] += "…"

                list_cleaned.append(splitted)


            elif "." in element:
                if ". " in element:
                    splitted = element.split(". ")
                    splitted[0] += "."
                else:

                    splitted = element.split(".")
                    splitted[0] += "."
                    if element.endswith("."):
                        splitted[1] += "."
                        del splitted[-1]

                list_cleaned.append(splitted)

            # if there is none of the above characters in the sentence
            else:
                ele = []
                for el in element:
                    ele.append(el)
                # joint the parts of the list
                joined = "".join(ele)
                joinie = []
                # append joined into a list
                joinie.append(joined)
                # append this list to another list (list in a list)
                list_cleaned.append(joinie)

        #print(list_cleaned)
                
        for elem in list_cleaned:

            # every elem in now a list cointaining strings
            #print(elem)

            # call the tokenize function with one joke at a time
            tokenize(elem)



def tokenize(sentences_str: List) -> List[List[str]]:
    # initiate an empty list
    tokenized_list = []
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
    filter_profanity(tokenized_list,file2)


def filter_profanity(tokenized: List[List[str]], filename: str) -> Tuple[List[List[str]], int]:
    # open file in read mode
    with open(file2, "r", encoding="UTF-8") as profs:
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
    # to print it more beautifully we add a newline char to the joke
    final += "\n"

    print(final)

    return final


if __name__ == '__main__':
   split_into_sentences(file)


