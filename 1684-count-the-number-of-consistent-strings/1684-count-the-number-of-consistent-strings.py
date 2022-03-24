class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        for i in range(len(words)):
            check_all = True
            for j in words[i]:
                check = False
                for k in allowed:
                    if j == k:
                        check = True
                    if check == True:
                        break;
                check_all = check_all and check
            if check_all == True:
                cnt += 1
        return cnt