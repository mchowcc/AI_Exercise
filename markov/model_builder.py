# model_builder.py
# Build a bigram model using PARALLEL LISTS (no dictionaries allowed)
# words: list of unique tokens
# followers: list of lists where followers[i] are the tokens that followed words[i]

from typing import List

ENDERS = [".", "!", "?"]


def read_corpus(path):
    # Reads text from a file and returns a list of strings

    # Open the file and read entire file into a single string (variable text)
    with open(path, "r") as f:
        text = f.read()

    # Lowercase text, replace newline characters with spaces, and (optional) remove commas.
    text = text.lower().replace("\n", " ").replace(",", "")

    # Put spaces around enders
    for ender in ENDERS:
        text = text.replace(ender, f" {ender} ")

    # Split into tokens and return the list
    tokens = text.split()
    return tokens


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

    for i in range(len(tokens) - 1):
        # Select the token at index i
        current_word = tokens[i]
        # Select the token that follows it
        next_word = tokens[i + 1]
        if current_word in words:
            # Find the index of `current_word` in `words` list
            idx = words.index(current_word)          # O(n) is fine for this exercise
            followers[idx].append(next_word)
        else:
            # We found a new word
            current_word_followers = [next_word]  # the list of followers of the current word

            # Add the word `current_word` to the end of list `words
            words.append(current_word)

            # Add `current_word_followers` to the end of `followers`
            followers.append([next_word])
    return words, followers


def build_trigram_model(tokens):
    states = []
    followers = []
    for i in range(len(tokens) - 2):
        state = (tokens[i], tokens[i+1])
        nxt = tokens[i+2]
        if state in states:
            idx = states.index(state)
            followers[idx].append(nxt)
        else:
            states.append(state)
            followers.append([nxt])
    return states, followers
