# Finding all anagrams in a given string
from collections import Counter


def anagrams_in_strings(string1: str, string2: str) -> list:
    target = min(string1, string2, key=len)
    longest = max(string1, string2, key=len)
    target_count, current_count = {}, {}
    for index in range(len(target)):
        target_count[target[index]] = 1 + target_count.get(target[index], 0)
        current_count[longest[index]] = 1 + current_count.get(longest[index], 0)

    res = [0] if target_count == current_count else []
    start = 0
    for end in range(len(target),len(longest)):
        current_count[longest[end]] = 1+ current_count.get(longest[end],0)
        current_count[longest[start]] -= 1

        if current_count[longest[start]] == 0:
            current_count.pop(longest[start])
        start += 1

        if current_count == target_count:
            res.append(start)
    return res


string1 = "cbaebabacd"
string2 = "abc"
print(anagrams_in_strings(string1, string2))
