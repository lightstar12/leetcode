class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i >= j:
                    continue
                if k == abs(nums[i] - nums[j]):
                    cnt += 1
        return cnt