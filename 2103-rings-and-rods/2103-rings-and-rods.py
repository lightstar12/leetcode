class Solution:
    def countPoints(self, rings: str) -> int:
        cnt = 10
        Rods = [[0 for RGB in range(3)] for NUM in range(10)]
        for i in range(0, len(rings), 2):
            if rings[i] == 'R':
                Rods[int(rings[i+1])][0] = 1
            elif rings[i] == 'G':
                Rods[int(rings[i+1])][1] = 1
            elif rings[i] == 'B':
                Rods[int(rings[i+1])][2] = 1
        for num in range(10):
            for rgb in range(3):
                if Rods[num][rgb] == 0:
                    cnt -= 1
                    break
        return cnt