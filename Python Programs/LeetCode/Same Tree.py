'''
Given the roots of two binary trees p and q, write a function to
check if they are the same or not. Two binary trees are considered
the same if they are structurally identical, and the nodes have the same value.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case: both nodes are null
        if not p and not q:
            return True
        # base case: one node is null
        if not p or not q:
            return False
        # check if the values of the nodes are the same
        if p.val != q.val:
            return False
        # check if the left and right subtrees are the same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)