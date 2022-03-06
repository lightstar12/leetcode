class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        senti = ''
        for j in range(len(indices)):
    	    for i in range(len(indices)):
	    	    if j - indices[i] == 0:
		    	    senti = senti + s[i]
        return senti