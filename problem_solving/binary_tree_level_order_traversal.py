# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        
        from collections import deque
        queue = deque()
        queue.append(root)
        
        while(len(queue) != 0):
            level_result = []
            next_level_queue = deque()
            
            while(len(queue) != 0):
                node = queue.popleft()
                level_result.append(node.val)
                
                if node.left:
                    next_level_queue.append(node.left)
                
                if node.right:
                    next_level_queue.append(node.right)
            
            result.append(level_result)
            queue = next_level_queue
        
        return result