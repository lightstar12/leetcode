class Solution:
    def minimumSum(self, num: int) -> int:
        str_num = str(num)
        num_list = []
        for i in range(len(str_num)):
            num_list.append(int(str_num[i]))
        sum = 0
        for i in range(2):
            sum = sum + min(num_list) * 10
            num_list.remove(min(num_list))
        for j in range(2):
            sum = sum + num_list[j]
        return sum