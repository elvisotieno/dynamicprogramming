# Begin by creating a TrieNode class which represents node in Trie

class TrieNode:
    def __init__(self,char):
        self.char = char
        self.is_end = False
        self.counter = 0
        self.children = {}


# Lets Implement Trie operations(insert, access/search)

class Trie(object):
    def __init__(self):
        self.root = TrieNode('')

    def insert(self,word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        #mark the end of the word
        node.is_end = True
        #update the count to show that we've seen this word
        node.counter += 1


    def dfs(self, node, prefix):
        # node is the node to start with
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))
        for child in node.children.values():
            self.dfs(child,prefix + node.char)


    def query(self, x):
        self.output = []
        node = self.root

        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        # traverse the trie to get all possible candidate that match the prefix
        self.dfs(node,x[:-1])

        #sort the results in a reverse in order to rank the word with their popularity
        return sorted(self.output, key=lambda x: x[1], reverse=True)

trie = Trie()
trie.insert('was')
trie.insert('word')
trie.insert('watch')
trie.insert('war')
trie.insert('what')
trie.insert('where')
trie.query('was')
print(trie.output)
