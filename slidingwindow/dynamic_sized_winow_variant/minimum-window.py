# Given two strings s & t, return a minimum window in s which contain all characters in t


def minimum_window(s: str, t: str) -> list:
    t_table, s_window = {}, {}
    for index in range(len(t)):
        t_table[t[index]] = t_table.get(t[index], 0) + 1
        s_window[t[index]] = s_window.get(t[index], 0)
    need = len(t)
    have = 0
    start = 0
    res, indices = len(s)+1, []
    for end in range(len(s)):
        if s[end] in s_window:
            s_window[s[end]] += 1
            if s_window[s[end]] == t_table[s[end]]:
                have += 1
        while have == need:
            # update our result
            current_result = s[start:end + 1]
            res, indices = min(len(current_result), res), [start, end]

            # lets pop last element of s from our s_window
            if s[start] in t_table:
                s_window[s[start]] -= 1
            if s[start] in t_table and s_window[s[start]] < t_table[s[start]]:
                have -= 1
            start += 1
    if res > len(s):
        return ""

    return indices


s="ADOBECODEBANC"
t="ABCD"
print(minimum_window(s,t))
