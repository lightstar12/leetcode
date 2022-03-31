class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        S = ""
        for i in s:
            S = S + i
            if i == ' ':
                k -= 1
                if k == 0:
                    S = S[:-1]
                    break
        return S