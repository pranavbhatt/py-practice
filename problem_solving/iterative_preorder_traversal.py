# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        st = []
        result = []
        if not root:
            return result
        st.append(root)
        while(len(st) != 0):
            node = st.pop()
            result.append(node.val)
            
            if node.right:
                st.append(node.right)
                node.right = None
                
            if node.left:
                st.append(node.left)
                node.left = None
        return result
