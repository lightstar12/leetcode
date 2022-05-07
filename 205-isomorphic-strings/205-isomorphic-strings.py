class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_ = [1]
        t_ = [1]
        
        for i in range(1, len(s)):
            for j in range(0, i):
                if s[i] == s[j]:
                    break
                else:
                    s_.append(i)
                    
        for k in range(1, len(t)):
            for l in range(0, k):
                if t[k] == t[l]:
                    break
                else:
                    t_.append(k)
                    
        return s_ == t_