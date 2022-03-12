class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        a = []
        b = s[:2]
        c = r = 1
        c = c + ord(s[3]) - ord(s[0])
        r = r + int(s[4]) - int(s[1])
        for i in range(c):
            if i != 0:
                b = b.replace(b[0], chr(ord(b[0])+1))
            b = b.replace(b[1], s[1])
            for j in range(r):
                if j != 0:
                    b = b[0] + str(int(b[1])+1)
                a.append(b)
        return a