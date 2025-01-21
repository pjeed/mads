# PYTHON ==================================================
# LEVEL 1 - 5 mins
def reverse_no_vowels(word):
    """
    :param word: any english word

    :return the word in reverse, while removing all the vowels (a, e, i, o, u)
    
    example: word = "hello world" - return = "dlrw llh"

    restriction - do not use the built in reverse function for lists
    hint - range(10, -1, -1) will allow iteration from 10 to 0
    """

    # write code here, remove pass statement at the end

    pass

# LEVEL 2 - 10 mins
def most_common_letters(word1, word2):
    """

    :param word1: an english word / string
    :param word2: an english word / string
    :return: list of most common letters in word1 and word2

    examples:
       word1 = common, word2 = commute, return = ['m'] # not 'c' since m occurs twice
       word1 = common, word2 = hat, return = [] # no common letters
       word1 = common, word2 = commotion, return = ['o', 'm'] # both m and o occur atleast twice in both  words
    """

    # write code here, remove pass statement at the end

    pass

# LEVEL 3 - 15 mins
def nine_hat(clues):
    """
    :param clues: list of clues, sufficient to solve the nine hat puzzle
    example: - clues = [
                    ['X1', 'Y1', 'Z1'], ['X2', 'Y2'], ['X3','Y','Z','X','Y','Z','X','Y','Z']
                ]

    The Game: - sequence of 9 symbols. A symbol is a combination of 'X', 'Y', 'Z' and 1, 2, 3.
    So X2 is a symbol.

    The sequence must consist of all 9 possible symbols only once.
    
    Given the clues, return a list of lists of comma seperate symbols that could possibly be the solution that fits all the clues/

    For the example above, since the last sequence ensures X, Y and Z are repeating in that order, and clue 1 says X1, X2 and X3 must be in order, and clue2 says Y2 must follow X2
    The solution is 2 possible sequences:

    solution = [['X3','Y3','Z3','X1','Y1','Z1','X2','Y2','Z2'],
                ['X3','Y3','Z3','X2','Y2','Z2','X1','Y1','Z1']]

    """

    # write code here, remove pass statement at the end

    pass


if __name__ == "__main__":

    # 1 ==============================
    print(reverse_no_vowels("hello world")) #dlrw llh
    
    # 2 ==============================
    print(most_common_letters("common", "commotion"))

    # 3 ==============================
    print(nine_hat([['X1', 'Y1', 'Z1'], ['X2', 'Y2'], ['X3','Y','Z','X','Y','Z','X','Y','Z']]))

# 
