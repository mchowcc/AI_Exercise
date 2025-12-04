# generator.py
# Generates text from a bigram model.

import random

import model_builder  # Needed for ENDERS

# For consistency, we define the list of enders in one file, and then import it to other files that need it.
ENDERS = model_builder.ENDERS


def choose_start_word(words):
    # words: a list of strings, example: ['to', 'be,', 'or', 'not', 'that', 'is', 'the', 'question', '.', 'i', 'think' ]
    # TODO: return a random word from the list, which is not in ENDERS

    return "to"   # TODO: replace "to" with the chosen random word


def generate_from_bigram(words, followers, n_tokens=40):
    # words: a list of strings, example: ['to', 'be,', 'or', 'not', 'that', 'is', 'the', 'question', '.', 'i', 'think' ]
    # followers: a list of lists, example: [
    #         ['be,', 'be,', 'fear', 'err', 'forgive,', 'repeat'], ['or', 'that'], ['not'],
    #         ['to', 'worth', 'kill', 'what', 'gold'], ['is', 'which', 'glitters'],
    #         ['the', 'not', 'power', 'fear', 'human,', 'not', 'the', 'other', 'money', 'mightier'],
    #         ...
    # the first list element are words that can follow the first word in the `words` list
    # the second list element are words that can follow the second word in the `words` list
    # etc
    # Returns a randomly generated sentence

    output = []
    # TODO:
    # 1. Pick a start word
    # 2. In a loop:
    #   2.1 Find the followers of the current word
    #   2.2 Choose a random follower and append it to `output`
    #   2.3 Loop ends when you hit punctuation or length limit
    # 3. After the loop ends, combine string in list `output` into a string
    output_string = ""
    # 5. Clean up the string

    return output_string


def cleanup_spacing(text):
    # Fix spaces and capitalize first letter.
    # TODO: For every item in ENDERS, remove space before it:
    #       replace " ." with ".", etc.

    # TODO: Replace duplicate spaces with a single space.

    # TODO: Capitalize first character.

    return text
