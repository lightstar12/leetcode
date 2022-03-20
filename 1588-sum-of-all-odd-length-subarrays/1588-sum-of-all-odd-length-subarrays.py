class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum = 0
        length = 1
        while length <= len(arr):
            for i in range(len(arr) - length + 1):
                for j in range(length):
                    sum += arr[i+j]
            length += 2
        return sum