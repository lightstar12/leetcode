# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def in_order_traversal(self, BST_list: list):
        def _in_order_traversal(root):
            if root is None:
                pass
            else:
                _in_order_traversal(root.left)
                BST_list.append(root.val)
                _in_order_traversal(root.right)
        _in_order_traversal(self)
        return BST_list
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        BST_list = []
        bet_sum = 0
        print(Solution.in_order_traversal(root, BST_list))
        for i in BST_list:
            if i >= low and i <= high:
                bet_sum = bet_sum + i
        return bet_sum