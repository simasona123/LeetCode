# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#Recursion

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.node(root, result)
        return result

    def node(self, tree, result):
            if tree == None and tree == None:
                return 
            result.append(tree.val)
            self.node(tree.left, result)
            self.node(tree.right, result)


#Iteration

  