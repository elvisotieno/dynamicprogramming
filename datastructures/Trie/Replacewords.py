#In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor
#For example, when the root "an" is followed by the successor word "other", we can form a new word "another".
#Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it.
#If a successor can be replaced by more than one root, replace it with the root that has the shortest length.
#Return the sentence after the replacement.

#Example 1:
#Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
#Output: "the cat was rat by the bat"

#We'll insert each root in the trie. Then, for each word in the sentence, we'll replace it with the first root we encounter upon traversal of the trie.
from collections import defaultdict

def replaceWords(self, roots, sentence):
    _trie = lambda: collections.defaultdict(_trie)
    trie = _trie()
    END = True
    for root in roots:
        cur = trie
        for letter in root:
            cur = cur[letter]
        cur[END] = root

    def replace(word):
        cur = trie
        for letter in word:
            if letter not in cur: break
            cur = cur[letter]
            if END in cur:
                return cur[END]
        return word

    return " ".join(map(replace, sentence.split()))

