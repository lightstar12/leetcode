class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if ((i != j) & (nums[i] == nums[j]) & ((i * j) % k == 0)):
                    cnt += 1
        return cnt