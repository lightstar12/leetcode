class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        for i in range(n):
            nums.append(start + 2 * i)
        c = nums[0]
        for i in range(1, len(nums)):
            c = c ^ nums[i]
        return c