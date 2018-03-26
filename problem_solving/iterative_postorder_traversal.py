# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        st = []
        postorder_st = []
        if not root:
            return postorder_st
        st.append(root)
        
        while(len(st) != 0):
            node = st.pop()
            postorder_st.append(node.val)
            
            if node.left:
                st.append(node.left)
                node.left = None
            
            if node.right:
                st.append(node.right)
                node.righ = None
        
        return postorder_st[::-1]
