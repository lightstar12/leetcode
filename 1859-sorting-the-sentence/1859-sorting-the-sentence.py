class Solution:
    def sortSentence(self, s: str) -> str:
        s_part = s.split()
        s__part = []
        for i in range(len(s_part)):
        	s__part.append(0)
        
        for j in range(len(s_part)):
            s__part[int(s_part[j][-1])-1] = s_part[j]
            
        for k in range(len(s_part)):
            s__part[k] = s__part[k][:-1]
        
        S = ' '.join(s__part)
        return S