# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    #finds solution through recursion
    def maxDepth(self, root):
        #base case
        if not root:
            return 0
        #recursion function of finding the depth of left and right sides, returning an integer
        else:
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
