# model_builder.py
# Build a bigram model using PARALLEL LISTS (no dictionaries allowed)
# words: list of unique tokens
# followers: list of lists where followers[i] are the tokens that followed words[i]

from typing import List

ENDERS = [".", "!", "?"]


def read_corpus(path):
    # Reads text from a file and returns a list of strings
    text = ""

    # TODO: Open the file and read entire file into a single string (variable text)

    # TODO: Lowercase text, replace newline characters with spaces, and (optional) remove commas.

    # Put spaces around enders
    for ender in ENDERS:
        text = text.replace(ender, f" {ender} ")

    # TODO: Split into tokens and return the list

    # TODO: Remove the line below:
    return ["to", "be", "or", "not", "to", "be", "that", "is", "the", "question", "."]  # For testing purpose only


def build_bigram_model(tokens):
    # tokens: list of strings, example: ["to", "be", "or", "not", "to", "be", "that",
    #       "is", "the", "question", ".", "i", "think,", "therefore", "i", "am", "."]
    # Function returns:
    # - a list of unique tokens (words)
    # - a parallel list of lists (followers)
    # Example:
    # ["to", "be", "or", "not", "that", "is", "the", "question", ".", "i", "think,", "therefore", "am"]
    # [ ["be", "be"], ["or", "that"], ["not"], ["to"], ["is"], ["the"], ["question"], ["."], ["i"],
    #   ["think", "am"], ["therefore"], ["i"], ["."]]
    # In this example, the word "to" can be followed by "be"
    #                  the word "be" can be followed by either "or" or "that"
    #                  ...
    #                  the word "i" can be followed by either "think" or "am"
    # Note the duplication - ["be", "be"] - this happens because there are two occurrences of the
    # word "to" followed be "be".
    # Using a larger input file, the followers of "to" might be:
    #    ['be', 'be', 'fear', 'err', 'forgive', 'repeat', 'an', 'the', 'each', 'those', 'be', 'live', 'learn']

    words = []
    followers = []
    current_word = ""
    next_word = ""
    idx = 0

    for i in range(len(tokens) - 1):
        # TODO: Select the token at index i
        # current_word =
        # TODO: Select the token that follows it
        # next_word =
        if current_word in words:
            # TODO: Find the index of `current_word` in `words` list
            # idx =
            followers[idx].append(next_word)
        else:
            # We found a new word
            current_word_followers = [next_word]  # the list of followers of the current word

            # TODO: Add the word `current_word` to the end of list `words

            # TODO: Add `current_word_followers` to the end of `followers`

    return words, followers
