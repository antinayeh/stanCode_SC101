"""
File: anagram.py
Name: Antina
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    ####################
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    word = input('Find anagrams for: ')
    start = time.time()

    while word != EXIT:
        print("Searching...")
        anagrams = find_anagrams(word)
        print(str(len(anagrams)) + ' anagrams: ' + str(anagrams))
        end = time.time()
        word = input('Find anagrams for: ')

    ####################
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    :return: list of words in FILE
    """
    d = []
    with open(FILE, 'r') as f:
        for line in f:
            d.append(line.strip())
    return d


def find_anagrams(s):
    """
    :param s: input word
    :return: list of anagrams for 's'
    """
    dictionary = read_dictionary()
    # create a dict of s that maps occurrence of each letter
    word_dict = {}
    for letter in s:
        if letter not in word_dict:
            word_dict[letter] = 1
        else:
            word_dict[letter] += 1
    anagram = helper(s, "", [], dictionary, word_dict)
    return anagram


def helper(input_word, current_word, anagram, dictionary, word_dict):
    """
    :param input_word: input word
    :param current_word: current word
    :param anagram: list of anagrams for word
    :param dictionary: list of words in dictionary
    :param word_dict: a dict that maps occurrence of each letter in input word
    :return: list of anagrams for input word
    """
    if len(current_word) == len(input_word):  # base case
        if current_word not in anagram and current_word in dictionary:
            # create a dict of current_word that maps occurrence of each letter
            current_dict = {}
            for letter in current_word:
                if letter not in current_dict:
                    current_dict[letter] = 1
                else:
                    current_dict[letter] += 1
            # compare two dicts that maps occurrence of each letter
            if current_dict == word_dict:
                print("Found: " + current_word)
                print("Searching: ")
                anagram.append(current_word)
    else:
        for letter in input_word:
            current_word += letter
            if has_prefix(current_word, dictionary):
                helper(input_word, current_word, anagram, dictionary, word_dict) # explore
            current_word = current_word[:len(current_word) - 1]  # unchoose
    return anagram


def has_prefix(sub_s, dictionary):
    """
    :param dictionary: dictionary of words
    :param sub_s: substring
    :return: true if word contains substring
    """
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False



if __name__ == '__main__':
    main()
