# Source: https://leetcode.com/problems/word-ladder/

# Problem: "Word Ladder"

# Example:
# Given two words (beginWord and endWord), and a dictionary's word list, 
# find the length of shortest transformation sequence from beginWord to 
# endWord, such that:
# 1. Only one letter can be changed at a time.
# 2. Each transformed word must exist in the word list.
# Example 1:
#   Input:
#     beginWord = "hit",
#     endWord = "cog",
#     wordList = ["hot","dot","dog","lot","log","cog"]
#   Output: 5
#   Explanation: As one shortest transformation is 
#   "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.
# Example 2:
#   Input:
#     beginWord = "hit"
#     endWord = "cog"
#     wordList = ["hot","dot","dog","lot","log"]
#   Output: 0
#   Explanation: The endWord "cog" is not in wordList, 
#   therefore no possible transformation.

# Approach: BFS, dict and creating all possible differences *

from collections import defaultdict, deque

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0
    L = len(beginWord)
    # Dictionary to hold combination of words that can be formed,
    # from any given word. By changing one letter at a time.
    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(L):
            # Key is the generic word
            # Value is a list of words which have the same intermediate generic word.
            all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
    queue = deque([(beginWord, 1)])
    visited = {beginWord: True}
    while queue:
        current_word, level = queue.popleft()      
        for i in range(L):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]
            # Next states are all the words which share the same intermediate state.
            for word in all_combo_dict[intermediate_word]:
                # If at any point if we find what we are looking for
                # i.e. the end word - we can return with the answer.
                if word == endWord:
                    return level + 1
                # Otherwise, add it to the BFS Queue. Also mark it visited
                if word not in visited:
                    visited[word] = True
                    queue.append((word, level + 1))
            all_combo_dict[intermediate_word] = []
    return 0