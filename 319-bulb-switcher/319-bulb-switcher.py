import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        cnt = 0
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return int(math.sqrt(n))