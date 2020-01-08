#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def isSymmetric(self, root):
        
        if not root: return True
        que = collections.deque()
        que.append(root.left)
        que.append(root.right)
        while que:
            left, right = que.popleft(), que.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return 
            if left.val != right.val:
                return False
            que.append(left.left)
            que.append(right.right)
            que.append(left.right)
            que.append(right.left)
        return True

