# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
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
            #peek: node
            node = st[len(st)-1]
            
            # node has left child?
            if node.left:
                st.append(node.left)
                node.left = None
                continue
            
            node = st.pop()
            result.append(node.val)
            
            # node has right child?
            if node.right:
                st.append(node.right)
                node.right = None
                
        return result
