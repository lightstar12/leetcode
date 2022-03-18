class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        nestcnt = 0
        for i in range(len(s)):
            if s[i] == '(':
                cnt += 1
            if nestcnt < cnt:
                nestcnt = cnt
            if s[i] == ')':
                cnt -= 1
        return nestcnt