class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while(num != 0):
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
            cnt = cnt + 1    
        return cnt