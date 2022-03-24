class Solution:
    def numberOfMatches(self, n: int) -> int:
        total = 0
        while n != 1:
            total += int(n/2)
            if n % 2 == 0:
                n = n / 2
            else:
                n = (n - 1) / 2 + 1
        return total