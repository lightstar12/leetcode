class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        u_cnt = 0
        v_cnt = 0
        for i in range(1, len(edges)):
            if edges[0][0] == edges[i][0]:
                u_cnt += 1
            if edges[0][1] == edges[i][1]:
                v_cnt += 1
        if u_cnt > v_cnt:   return edges[0][0]
        elif u_cnt < v_cnt: return edges[0][1]