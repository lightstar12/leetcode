class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal = ''
        L_cnt = 0
        R_cnt = 0
        cnt = 0
        for i in s:
            if i == 'L':
                L_cnt = L_cnt + 1
                bal = bal + i
                if L_cnt == R_cnt:
                    cnt = cnt + 1
                    bal = ''
            elif i == 'R':
                R_cnt = R_cnt + 1
                bal = bal + i
                if R_cnt == L_cnt:
                    cnt = cnt + 1
                    bal = ''
        return cnt