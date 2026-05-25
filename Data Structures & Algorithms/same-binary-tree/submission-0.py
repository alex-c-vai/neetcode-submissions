# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pathP = []
        pathQ = []

        def dfs(root, path):
            if root == None:
                path.append(root)
                return
            path.append(root.val)
            dfs(root.left, path)
            dfs(root.right, path)
            return
        
        dfs(p, pathP)
        dfs(q, pathQ)
        return pathP == pathQ