class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        Word1 = ''
        Word2 = ''
        for i in word1:
            Word1 = Word1 + i
        for j in word2:
            Word2 = Word2 + j
        if Word1 == Word2:
            return True
        else:
            return False