# generator.py
# Generates text from a bigram model.

import random

import model_builder  # Needed for ENDERS

# For consistency, we define the list of enders in one file, and then import it to other files that need it.
ENDERS = model_builder.ENDERS


def choose_start_word(words):
    # words: a list of strings, example: ['to', 'be,', 'or', 'not', 'that', 'is', 'the', 'question', '.', 'i', 'think' ]
    # Return a random word from the list, which is not in ENDERS
    candidates = [w for w in words if w not in ENDERS]
    if not candidates:
        raise ValueError("Corpus must contain at least one non-terminating token")
    return random.choice(candidates)


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
    # Pick a start word
    current = choose_start_word(words)
    output.append(current)

    # Speed up follower lookups by mapping each word to its follower list
    follower_map = {word: options for word, options in zip(words, followers)}

    while len(output) < n_tokens and current not in ENDERS:
        options = follower_map.get(current)
        if not options:
            break

        # Choose a random follower and append it to `output`
        nxt = random.choice(options)
        output.append(nxt)
        current = nxt
        if nxt in ENDERS:
            break

    # After the loop ends, combine string in list `output` into a string
    output_string = " ".join(output)

    # Clean up the string
    output_string = cleanup_spacing(output_string)
    return output_string


def cleanup_spacing(text):
    # Fix spaces and capitalize first letter.
    # For every item in ENDERS, remove space before it:
    for ender in ENDERS:
        text = text.replace(" " + ender, ender)

    # Replace duplicate spaces with a single space.
    while "  " in text:
        text = text.replace("  ", " ")

    # Capitalize first character.
    try:
        text = text[0].upper() + text[1:]
    except IndexError:
        pass
    return text
