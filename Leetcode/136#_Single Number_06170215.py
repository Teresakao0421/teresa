#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def singleNumber(self, A):
        ans = A[0]
        for i in range(1, len(A)):
            ans = ans ^ A[i]
        return ans

