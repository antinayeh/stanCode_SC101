"""
File: boggle.py
Name: Antina
----------------------------------------
TODO:
"""
import sys
import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
    TODO:
    """
    start = time.time()
    ####################
    matrix = []
    for i in range(1, 5):
        letters = input(str(i) + " row of letters: ")
        row = []
        count = 1
        for ch in letters:
            if (count % 2 == 0 and ch != " ") or (count % 2 != 0 and not ch.isalpha()):
                print('Illegal input')
                sys.exit()
            if count % 2 != 0:
                ch = ch.lower()
                row.append(ch)
            count += 1
        if len(row) != 4:
            sys.exit()
        matrix.append(row)
    word_list = boggle(matrix)
    print("There are " + str(len(word_list)) + " words in total")

    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def boggle(matrix):
    d = read_dictionary()
    word_dict = {}
    word_list = []

    for row in matrix:
        for letter in row:
            if letter not in word_dict:
                word_dict[letter] = 1
            else:
                word_dict[letter] += 1

    for r in range(0, 4):
        for c in range(0, 4):
            current = matrix[r][c]
            visited = [(r, c)]
            word_list.append(helper(matrix, current, [], word_dict, d, r, c, visited))

    ans = []
    for l in word_list:
        for w in l:
            if w not in ans:
                ans.append(w)
    return ans


def helper(matrix, current, word_list, word_dict, dictionary, r, c, visited):
    """
    :param matrix: 4 x 4 matrix of input letters
    :param current:  current string
    :param word_list: list of found words
    :param word_dict: dict of each letter and frequency
    :param dictionary: dict of all words
    :param r: starting row
    :param c: starting column
    :param visited: all visited coordinates
    :return: list of found words
    """
    found = False
    if len(current) >= 4 and current not in word_list:
        if current in dictionary[current[0]]:
            print("Found: " + current)
            word_list.append(current)
            found = True

    if len(current) < 4 or found:
        for x in range(r - 1, r + 2):
            for y in range(c - 1, c + 2):
                if -1 < x < 4 and -1 < y < 4:
                    if (x, y) not in visited or (x == r and y == c):
                        ch = matrix[x][y]
                        if current.count(ch) + 1 <= word_dict[ch]:
                            if current.count(ch) == 0 or (current.count(ch) > 0 and (x != r and y != c)):
                                current += matrix[x][y]
                                visited.append((x, y))
                                if has_prefix(current, dictionary):
                                    helper(matrix, current, word_list, word_dict, dictionary, x, y, visited)
                                current = current[:len(current) - 1]
                                visited = visited[:len(current) - 1]
    return word_list


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    d = {}
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) > 3:
                letter = line[0]
                if letter not in d:
                    d[letter] = [line]
                else:
                    d[letter].append(line)
    return d


def has_prefix(sub_s, dictionary):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    word_list = dictionary[sub_s[0]]
    for word in word_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
