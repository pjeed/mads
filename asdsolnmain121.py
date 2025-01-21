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
    result = ""
    
    for i in range(len(word)-1, -1, -1):
        if word[i] not in ['a', 'e','i','o', 'u']:
            result += word[i]

    return result


# LEVEL 2 - 20 mins
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

    result = []
    max_count = 0

    common_letters = []
    
    #
    letter_map_word1 = {}
    letter_map_word2 = {}
    # write code here, remove pass statement at the end
    for i in range(len(word1)):
        if word1[i] in letter_map_word1:
            letter_map_word1[word1[i]] += 1
        else:
            letter_map_word1[word1[i]] = 1

    for i in range(len(word2)):
        if word2[i] in letter_map_word2:
            letter_map_word2[word2[i]] += 1
        else:
            letter_map_word2[word2[i]] = 1
        
        if word2[i] in letter_map_word1 and word2[i] not in common_letters:
            common_letters.append(word2[i])
    
    for cl in common_letters:
        num_times = min(letter_map_word1[cl],  letter_map_word2[cl])
        if num_times > max_count:
            max_count = num_times
            result = [cl]
        elif num_times == max_count:
            result.append(cl)



    return result

if __name__ == "__main__":

    # 1 ==============================
    print(reverse_no_vowels("hello world")) #dlrw llh
    
    # 2 ==============================
    print(most_common_letters("common", "commute")) #['m']
    print(most_common_letters("common", "hat"))#[]
    print(most_common_letters("common", "commotion"))#['o', 'm']
