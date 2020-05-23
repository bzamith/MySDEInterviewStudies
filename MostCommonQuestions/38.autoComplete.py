# Source: https://www.youtube.com/watch?v=QGVCnjXmrNg
# Source: https://www.byte-by-byte.com/autocomplete/

# Problem: "Autocomplete"

# Example: Write an autocomplete class that returns all 
# dictionary words with a given prefix.
# dict:   {"abc", "acd", "bcd", "def", "a", "aba"}
# prefix: "a" -> "abc", "acd", "a", "aba"
# prefix: "b" -> "bcd"

# Brute-force Solution: Iterate over each word in dict

# Approach: Trie data structure (tree)

class Node():
    def __init__(self, prefix):
        self.prefix = prefix
        self.children = {}
        #Does this node represent the last character in a word?
        self.isWord = False

class Solution():
    def __init__(self):
        self.trie = None
        self.results = []

    def constructTrie(self, dictionary):
        self.trie = Node('')
        for string in dictionary:
            self.insertWord(string)

    def insertWord(self, string):
        # Iterate through each character in the string. If the character is not
        # already in the trie then add it
        currNode = self.trie
        for i in range(len(string)):
            if string[i] not in currNode.children:
                currNode.children[string[i]] = Node(string[0:i+2])
            currNode = currNode.children[string[i]]
            if i == len(string) - 1:
                currNode.isWord = True

    def getWordsForPrefix(self, prefix):
        self.results = []
        curr = self.trie
        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return self.results
        self.findAllChildWords(curr)
        return self.results
        
    def findAllChildWords(self, node):
        if node.isWord:
            self.results.append(node.prefix)
        for char in node.children.keys():
            self.findAllChildWords(node.children[char])

if __name__ == '__main__':
    sol = Solution()
    sol.constructTrie(["abc", "acd", "bcd", "def", "a", "aba"])
    print(sol.getWordsForPrefix("a"))
    print(sol.getWordsForPrefix("d"))
