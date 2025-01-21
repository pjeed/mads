import re
import json

# LEVEL 1
def reverse_no_vowels(word):
    """
    :param word: any english word

    :return the word in reverse, while removing all the vowels (a, e, i, o, u)
    
    example: word = "hello world" - return = "dlrw llh"
    """

    return None

# LEVEL 2
def count_elements(element_list, to_count):
    """

    :param element_list: a list of elements ex. [1, 2, "cat", "dog", 1, 1, "cat", "horse"]
    :param to_count: any item that may or may not be in the element_list - ex. "cat"
    :return: number of times "to_count" element appears in element_list ex. 2
    """

    # write code here, remove pass statement at the end

    pass

# LEVEL 3
def find_total_cost(data):
    """
    :param data:
    is a JSON string in this format:
    [
        {
            "instances": 10,
            "cost": 100
        },
        {
            "instances": 5,
            "cost": 20
        }
    ]
    :return: Total cost of everything. (sum of all instances*cost_per)
    - ex. for above = (10*100)+(5*20) = 1000 + 100 = 1100

    hint - convert data from string to dictionary/map using json.loads
    """

    # write code here, remove pass statement at the end

    pass


# LEVEL 4
def get_short_code(long_code):
    """
    :param long_code: <text>#_<text>#, ex. zone4_subnet1
    :return: #-#, ex. 4-1 or None if text is not a valid code
    hint - regex to match long_code is '[a-z]+(\d+)_[a-z]+(\d+)'
    hint 2 -
        matches = re.match('[a-z]+(\d+)_[a-z]+(\d+)', long_code, re.IGNORECASE)
        matches.group(1) gives you the first number, matches.group(2) gives you the second number
        matches is None if no matches are found
    """
    
    # write code here, remove pass statement at the end

    pass

if __name__ == "__main__":

    # 1 ==============================
    print(reverse_no_vowels("hello world")) #dlrw llh
    
    # 2 ==============================
    print(count_elements([1,0,1,0,1,1,1], 1)) # 5

    # 3 ==============================
    data = [{"instances": 1, "cost": 1000}, {"instances": 2, "cost": 500}, {"instances": 5, "cost": 200}]
    print(find_total_cost(json.dumps(data)))  # 3000

    # 4 =======================
    short_code = get_short_code("zone42_subnet123")
    print(short_code)# 42-123

# 
