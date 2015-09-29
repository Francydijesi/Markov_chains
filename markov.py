from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    content = open(file_path).read()
    content = content.replace('\n', ' ')
    return content


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    words = text_string.split()

    for index in range(len(words)-2):
        key = (words[index], words[index+1])
        value = words[index+2]

        if key in chains.keys():
            chains[key].append(value)
        else:
            chains[key] = [value]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    
    text = ""
    first_key = choice(chains.keys())
    third_word = choice(chains[first_key])
    
    text += first_key[0] + " " + first_key[1] + " " + third_word + " "
    new_key = (first_key[1], third_word)

    while new_key in chains:
        next_word = choice(chains[new_key])
        text += next_word + " "

        new_key = (new_key[1], next_word)
    
    return text


input_path = "green-eggs.txt"
# input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
