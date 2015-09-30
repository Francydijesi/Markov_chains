from random import choice
import sys


def open_and_read_file(file_path_list):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    content = ""
    
    for file_path in file_path_list:
        content = content + " " + open(file_path).read()
          
    content.replace('\n', ' ')  
    return content


def make_chains(text_string, n):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    print n
    chains = {}
    words = text_string.split()

    for index in range(len(words)-n):        
        key_list = []

        for i in range(n):
            key_list.append(words[index + i])
        
        key = tuple(key_list)
        value = words[index + n]
        # key = (words[index], words[index+1])
        # value = words[index+2]

        if key in chains.keys():
            chains[key].append(value)
        else:
            chains[key] = [value]
    print chains
    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    
    text = ""
    first_key = choice(chains.keys())
    next_word = choice(chains[first_key])
    
    words_in_tuple = []

    # for word in first_key:
    #     words_in_tuple.append(word)

    text += " ".join(first_key) + " " + next_word + " "
    
    # Creates a new key
    new_key = first_key[1:] + (next_word,)
    
    while new_key in chains:
        next_word = choice(chains[new_key])
        text += next_word + " "

        new_key = new_key[1:] + (next_word,)

    if text[-1].isalpha():
        text + "."

    return text[0].upper() + text[1:]


input_paths = []
ngrams = 2

if len(sys.argv) > 2:
   ngrams = int(sys.argv[1])  
   for arg in sys.argv[2:]:
       input_paths.append(arg)
else:
    input_path.append("gettysburg.txt")
    
# input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_paths)

# Get a Markov chain
chains = make_chains(input_text,ngrams)

# Produce random text
random_text = make_text(chains)

print random_text



# make_text => aribtrary n-grams
# python markov.py 3 file1.txt file2.txt