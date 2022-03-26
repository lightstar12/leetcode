class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        alphabet = [0 for i in range(26)]
        for s in range(len(sentence)):
            alphabet[ord(sentence[s]) - 97] += 1
        for a in range(len(alphabet)):
            if alphabet[a] == 0:
                return False
        return True