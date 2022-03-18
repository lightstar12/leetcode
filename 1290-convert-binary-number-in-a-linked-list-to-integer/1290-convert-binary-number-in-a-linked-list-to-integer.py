# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        List = []
        List.append(head.val)
        LisT = head.next
        while LisT != None:
            List.append(LisT.val)
            LisT = LisT.next
        demical = 0
        for i in range(len(List)):
            demical += List[i] * (2 ** (len(List) - i - 1))
        return demical