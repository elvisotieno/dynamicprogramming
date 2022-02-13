# Anagramatic pairs of strings
#Let’s summarize the approach:

#We need to find all substrings of the given string — create a method for that.
#We need to be able to check if two strings are anagrams — create a method for that.
#We need to count all anagrammatic pairs in the given string — create a method for that.
#Combine everything from above and split the result — create a method for that.

from collections import Counter
# all substrings in a given string

def get_all_substrings(s):
    return [[s[col:col + row] for col in range(len(s) - row + 1)] for row in range(1, len(s))]


def check_for_anagrams(string1, string2):
    hist1 = Counter(string1)
    string2=list(string2)
    hist1.subtract(string2)
    for val in hist1.values():
        if val:
            return False
    return True


def count_anagramatic_pair(current_index, arr):
    current_element= arr[current_index]
    arr_Rest = arr[current_index+1:]
    counter = 0
    for i in range(len(arr_Rest)):
        if len(current_element) == len(arr_Rest[i]) and check_for_anagrams(current_element, arr_Rest[i]):
            counter += 1

    return counter


def sharelock_and_anagrams(s):
    new_list= list(s)
    uniques=[]
    is_duplicate = False
    for element in new_list:
        if element not in uniques:
            uniques.append(element)
        else:
            is_duplicate = True
    if not is_duplicate:
        return 0
    anagram_count = 0
    arr = get_all_substrings(s)
    for i in range(len(arr)):
        anagram_count += count_anagramatic_pair(i, arr)
    return anagram_count


string1 = 'silent'
string2 = 'listen'
print(check_for_anagrams(string1, string2))